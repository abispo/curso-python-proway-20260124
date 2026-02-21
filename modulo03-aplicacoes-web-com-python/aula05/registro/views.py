from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse

from . import forms
from .models import PreRegistro
from .utils import enviar_email

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

            pre_registro_valido_ja_existe = PreRegistro.objects.filter(
                email=email, valido=True
            ).exists()

            if pre_registro_valido_ja_existe:
                return render(
                    request,
                    "registro/pre_registro.html",
                    {
                        "form": forms.PreRegistroForm,
                        "erros": [
                            "Já existe um pré-registro com esse e-mail, finalize ou aguarde o link expirar."
                        ]
                    }
                )
            
            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            enviar_email(request, pre_registro)

            return redirect(reverse(
                "registro:envio_email_pre_registro"
            ))

def envio_email_pre_registro(request):
    return render(
        request,
        "registro/envio_email_pre_registro.html"
    )

def confirmar_registro(request):
    return render(
        request,
        "registro/confirmar_registro.html"
    )