import uuid

from django.db import models

from base.models import DiscordUser


class Entry(models.Model):
    slug = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_for = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entry(slug='{self.slug}', created_for={self.created_for})"

    class Meta:
        unique_together = ["repo", "slug"]
