from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from . import forms

def pre_registro(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "registro/pre_registro.html",
        {"form": forms.PreRegistroForm}
    )
