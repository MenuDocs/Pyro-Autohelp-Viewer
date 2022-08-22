from django.db import models

from base.models import Case


class CodeError(models.Model):
    """The errors in specific cases."""

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="errors")
    title = models.TextField(help_text="A short title describing this error.")
    description = models.TextField(
        help_text="A more in depth piece of text describing this error."
    )
    old_code_link = models.URLField(help_text="A link to the original code.")
    fixed_code_link = models.URLField(help_text="A link to the fixed code.")

    def __str__(self):
        return f"CodeError(title='{self.title}', case={self.case})"
