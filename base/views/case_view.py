from django.http import HttpRequest
from django.shortcuts import render


def case_view(request: HttpRequest, slug: str):
    return render(request, "base/index.html")
