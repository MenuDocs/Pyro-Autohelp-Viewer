from django.urls import path

from api.api import API

urlpatterns = [
    path("", API.urls),
]
