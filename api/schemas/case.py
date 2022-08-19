import datetime

from ninja import Schema, Field
from pydantic import HttpUrl

from api.schemas import CodeErrorInSchema, DiscordUserSchema


class CaseInSchema(Schema):
    errors: list[CodeErrorInSchema]
    created_for: DiscordUserSchema


class CaseOutSchema(CaseInSchema):
    slug: str = Field(..., description="The URL slug for this entry.")
    created_at: datetime.datetime = Field(
        ..., description="When this entry was created."
    )
    last_edited_at: datetime.datetime = Field(
        ..., description="When this entry was last edited."
    )


class PartialCaseSchema(Schema):
    slug: str = Field(..., description="The URL slug for this entry.")
    view_url: HttpUrl = Field(
        ..., description="The URL for the end user to view this case.html."
    )
