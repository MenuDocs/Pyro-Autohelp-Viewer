from django.urls import path

from base.views import index_view

urlpatterns = [
    path("", index_view),
    path("cases/<slug:str>", index_view, name="base-view_case"),
]
