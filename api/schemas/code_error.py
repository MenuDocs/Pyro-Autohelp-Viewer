from ninja import Schema, Field
from pydantic import HttpUrl


class CodeErrorInSchema(Schema):
    message: str = Field(..., description="A message.py describing this error.")
    old_code_link: HttpUrl = Field(..., description="A link to the original code.")
    fixed_code_link: HttpUrl = Field(..., description="A link to the fixed code.")


class CodeErrorOutSchema(CodeErrorInSchema):
    entry_slug: str = Field(..., description="The UUID")
