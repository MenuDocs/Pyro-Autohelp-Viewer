import os

from django.conf import settings
from ninja.security import APIKeyHeader


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        required_key = os.environ.get("API_KEY")
        if settings.DEBUG and not required_key:
            required_key = "test_key"

        if key == required_key:
            return key
