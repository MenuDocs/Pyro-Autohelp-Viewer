from django.http import HttpRequest

from base.util import render_template


def about_view(request: HttpRequest):
    return render_template(request, "base/about.html", current_nav_link="About")
