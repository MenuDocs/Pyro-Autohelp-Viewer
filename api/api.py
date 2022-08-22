import orjson
from django.core.exceptions import PermissionDenied, BadRequest, ValidationError
from django.http import Http404, HttpRequest
from ninja import NinjaAPI
from ninja.parser import Parser
from ninja.renderers import BaseRenderer

from api.auth import ApiKey
from api.schemas import (
    CaseInSchema,
    PartialCaseSchema,
    Message,
    PydanticValidationMessage,
    CaseOutSchema,
)
from base.models import DiscordUser, CodeError, Case


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


API = NinjaAPI(
    title="Pyro Automated help API",
    version="1.0.0",
    parser=ORJSONParser(),
    renderer=ORJSONRenderer(),
    auth=ApiKey(),
)


@API.exception_handler(Http404)
def handle_404(request, exc):
    return API.create_response(request, {"detail": str(exc)}, status=404)


@API.exception_handler(PermissionDenied)
def handle_404(request, exc):
    return API.create_response(request, {"detail": str(exc)}, status=403)


@API.exception_handler(BadRequest)
def handle_400(request, exc):
    return API.create_response(request, {"detail": str(exc)}, status=400)


@API.post(
    "cases",
    summary="Create a new case",
    description="Creates a new case which can be viewed by the end user.",
    tags=["Cases"],
    response={201: PartialCaseSchema, 401: Message, 422: PydanticValidationMessage},
)
def create_case(request: HttpRequest, entry: CaseInSchema):
    discord_user, created = DiscordUser.objects.get_or_create(
        user_id=entry.created_for.user_id,
        defaults={
            "user_id": entry.created_for.user_id,
            "last_known_name": entry.created_for.last_known_name,
        },
    )
    if not created and entry.created_for.last_known_name:
        # If we already have the user and a new name, update it.
        discord_user.last_known_name = entry.created_for.last_known_name
        discord_user.save()
        discord_user.refresh_from_db()

    case: Case = Case(created_for=discord_user)
    case.save()
    case.refresh_from_db()

    errors: list[CodeError] = []
    for error in entry.errors:
        errors.append(
            CodeError(
                case=case,
                title=error.title,
                description=error.description,
                old_code_link=error.old_code_link,
                fixed_code_link=error.fixed_code_link,
            )
        )

    CodeError.objects.bulk_create(errors)

    return 201, case.as_partial_schema(request)


@API.get(
    "cases/{slug}",
    summary="Fetch an entire case",
    description="Fetches and returns a stored case.",
    tags=["Cases"],
    response={
        200: CaseOutSchema,
        401: Message,
        422: PydanticValidationMessage,
        404: Message,
    },
    auth=None,
)
def fetch_case(request: HttpRequest, slug: str):
    try:
        case: Case = Case.objects.get(slug=slug)
    except (ValidationError, Case.DoesNotExist):
        raise Http404(f"Cannot find a case for slug '{slug}'")

    return case.as_schema(request)


@API.get(
    "cases/{slug}/partial",
    summary="Partially fetch a case",
    description="Fetches the view url for the given case. "
    "Use this over raw formatting for if the route changes internally.",
    tags=["Cases"],
    response={
        200: PartialCaseSchema,
        401: Message,
        422: PydanticValidationMessage,
        404: Message,
    },
    auth=None,
)
def fetch_partial_case(request: HttpRequest, slug: str):
    try:
        case: Case = Case.objects.get(slug=slug)
    except (ValidationError, Case.DoesNotExist):
        raise Http404(f"Cannot find a case for slug '{slug}'")

    return 200, case.as_partial_schema(request)
