from django.db import models

from base.models import Case


class CodeError(models.Model):
    """The errors in specific cases."""

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    message = models.TextField(help_text="A message.py describing this error.")
    old_code_link = models.URLField(help_text="A link to the original code.")
    fixed_code_link = models.URLField(help_text="A link to the fixed code.")

    def __str__(self):
        return f"CodeError(message.py='{self.message}', case={self.case})"
