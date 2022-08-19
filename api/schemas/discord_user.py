from typing import Optional

from ninja import Schema, Field


class DiscordUserSchema(Schema):
    user_id: int = Field(..., description="The user id of this person.")
    last_known_name: Optional[str] = Field(
        None, description="The name of this user if known."
    )
