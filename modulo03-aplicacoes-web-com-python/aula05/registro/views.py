from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse

from . import forms

# Apesar de não ser obrigatório, podemos indicar o tipo dos parâmetros de funções e também o tipo de retorno. Muitos consideram uma boa prática, e é muito útil também no uso de IDEs que não conseguem automaticamente inferir o tipo de dado que está sendo tratado.
def pre_registro(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(
            request,
            "registro/pre_registro.html",
            {"form": forms.PreRegistroForm}
        )
    
    elif request.method == "POST":
        form = forms.PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            return redirect(reverse(
                "registro:pre_registro"
            ))
