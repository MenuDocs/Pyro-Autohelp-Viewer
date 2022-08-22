from typing import Optional, Literal

from django.http import HttpRequest
from django.shortcuts import render

nav_links: list[dict[Literal["name", "url"], str]] = [
    {"name": "Home", "url": "/"},
    {"name": "About", "url": "/about"},
    {"name": "API documentation", "url": "/api/docs"},
]


def render_template(
    request: HttpRequest,
    file_path: str,
    *,
    context: Optional[dict] = None,
    current_nav_link: Optional[Literal["Home", "About", "API documentation"]] = None
):
    context = context or {}
    context["nav_links"] = nav_links
    context["current_nav_link"] = current_nav_link

    if request.user.is_staff:
        context["nav_links"].append({"name": "Admin", "url": "/admin"})

    return render(request, file_path, context=context)
