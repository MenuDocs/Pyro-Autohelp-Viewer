import uuid

from django.db import models
from django.urls import reverse

from api.schemas import PartialCaseSchema
from base.models import DiscordUser


class Case(models.Model):
    slug = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_for = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case(slug='{self.slug}', created_for={self.created_for})"

    def as_partial_schema(self) -> PartialCaseSchema:
        return PartialCaseSchema(
            slug=self.slug,
            view_url=reverse("base-view_case", kwargs={"slug": self.slug}),
        )
