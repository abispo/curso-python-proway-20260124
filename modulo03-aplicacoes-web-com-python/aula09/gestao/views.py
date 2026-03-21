from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrdemDeServico

def index(request: HttpRequest):
    return render(
        request,
        "gestao/index.html"
    )

def nova_ordem_de_servico(request: HttpRequest):

    if request.method == "GET":
        return render(
            request,
            "gestao/nova_ordem_de_servico.html"
        )
    
    elif request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")

        os = OrdemDeServico(
            titulo=titulo,
            descricao=descricao,
            cliente=request.user
        )

        os.save()

        return redirect(reverse("gestao:nova_ordem_de_servico"))