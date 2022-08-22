import uuid

from django.db import models
from django.http import HttpRequest
from django.urls import reverse

from api.schemas import PartialCaseSchema
from base.models import DiscordUser


class Case(models.Model):
    slug = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_for = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    @property
    def creator_name(self) -> str:
        """Saves us showing 'None' on the UI"""
        return (
            self.created_for.last_known_name
            if self.created_for.last_known_name
            else "Unknown User"
        )

    @property
    def slug_as_url_safe(self) -> str:
        return str(self.slug)

    def __repr__(self):
        return f"Case(slug='{self.slug}', created_for={self.created_for})"

    def __str__(self):
        return f"Case '{self.slug}'"

    def as_partial_schema(self, request: HttpRequest) -> PartialCaseSchema:
        return PartialCaseSchema(
            slug=self.slug_as_url_safe,
            view_url=request.build_absolute_uri(
                reverse("base-view_case", kwargs={"slug": self.slug_as_url_safe})
            ),
        )
