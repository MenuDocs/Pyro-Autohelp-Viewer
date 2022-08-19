from django.db import models


class DiscordUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    last_known_name = models.TextField()

    def __str__(self):
        return f"DiscordUser(user_id={self.user_id}, last_known_name='{self.last_known_name}')"
