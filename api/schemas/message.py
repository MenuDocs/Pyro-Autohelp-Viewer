from ninja import Schema, Field


class Message(Schema):
    detail: str = Field(..., description="Information regarding what happened.")
