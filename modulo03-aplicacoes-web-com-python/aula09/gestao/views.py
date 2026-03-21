from django.contrib import messages
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

        messages.success(
            request=request,
            message=f"Ordem de serviço #{os.pk} criada com sucesso."
        )

        return redirect(reverse("gestao:ordens_de_servico"))
    

class OrdemDeServicoListView(LoginRequiredMixin, ListView):
    model = OrdemDeServico
    template_name = 'gestao/lista_ordens.html'
    context_object_name = 'ordens_de_servico'

    def get_queryset(self):
        """
        Docstring for get_queryset
        
        Estamos modificando o método herdado get_queryset. Abaixo é verificado se o usuário tem a permissão 'gestao.pode_visualizar_todas_os'. Se ele tiver, todos os dados da model serão mostrados. Se não, vamos filtrar apenas as ordens de serviço criadas pelo próprio usuário.
        """
        user = self.request.user

        if user.has_perm("gestao.pode_visualizar_todas_os"):
            return OrdemDeServico.objects.all()
        
        return OrdemDeServico.objects.filter(cliente=user)
    
