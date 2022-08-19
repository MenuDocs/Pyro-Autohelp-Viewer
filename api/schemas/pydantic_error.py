from ninja import Schema, Field


class IssueSchema(Schema):
    loc: list[str] = Field(
        ...,
        description="Where in the request the issue is. This is a dotted dict path.",
    )
    msg: str = Field(..., description="The error.")
    type: str = Field(..., description="The type of error.")


class PydanticValidationMessage(Schema):
    detail: list[IssueSchema]
