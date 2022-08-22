from django.http import HttpRequest

from base.util import render_template


def index_view(request: HttpRequest):
    return render_template(request, "base/index.html", current_nav_link="Home")
