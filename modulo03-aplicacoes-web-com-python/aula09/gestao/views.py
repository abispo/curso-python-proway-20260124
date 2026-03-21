from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

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
    

class OrdemDeServicoListView(LoginRequiredMixin, ListView):
    model = OrdemDeServico
    template_name = 'gestao/lista_ordens.html'
    context_object_name = 'ordens'
