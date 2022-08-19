from django.core.exceptions import ValidationError
from django.http import HttpRequest, Http404
from django.shortcuts import render

from base.models import Case


def case_view(request: HttpRequest, slug: str):
    try:
        case: Case = Case.objects.get(slug=slug)
    except (Case.DoesNotExist, ValidationError):
        raise Http404

    return render(request, "base/case.html", context={"case": case})
