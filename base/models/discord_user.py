from django.db import models


class DiscordUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    last_known_name = models.TextField(null=True)

    def __str__(self):
        name = f"'{self.last_known_name}'" if self.last_known_name else None
        return f"DiscordUser(user_id={self.user_id}, last_known_name={name})"
