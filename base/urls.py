from django.urls import path

from base.views import index_view, repo_view, entry_view

urlpatterns = [
    path("", index_view),
    path("<str:repo_slug>", repo_view),
    path("<str:repo_slug>/<str:entry_slug>", entry_view),
]
