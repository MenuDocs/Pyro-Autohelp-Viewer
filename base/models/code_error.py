from django.db import models

from base.models import Entry


class CodeError:
    """The errors in specific entries."""

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    message = models.TextField()
    old_code_link = models.URLField(help_text="A link to the original code.")
    fixed_code_link = models.URLField(help_text="A link to the fixed code.")

    def __str__(self):
        return f"CodeError(message='{self.message}', entry={self.entry})"
