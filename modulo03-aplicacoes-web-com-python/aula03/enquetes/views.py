from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Opcao, Pergunta, Comentario

def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by(
        "-data_publicacao"
    )[:5]

    contexto = {
        "ultimas_cinco_perguntas": ultimas_cinco_perguntas,
    }

    return render(request, "enquetes/index.html", context=contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/detalhes.html", context={"pergunta": pergunta})

def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/resultados.html",
        {"pergunta": pergunta}
    )

def votar(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        opcao_escolhida = pergunta.opcao_set.get(pk=request.POST['opcao'])

    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você deve escolher uma opção"
            }
        )
    else:
        opcao_escolhida.votos = opcao_escolhida.votos + 1
        opcao_escolhida.save()

        return HttpResponseRedirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )
    
def recebe_comentario_pergunta(request, pergunta_id):

    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    texto_comentario: str = request.POST.get('texto_comentario')

    if len(texto_comentario.strip()) == 0:
        return render(
        request,
        "enquetes/resultados.html",
        {
            "pergunta": pergunta,
            "mensagem_erro": "Você deve informar o comentário antes de tentar enviar."
        }
    )

    comentario = Comentario(
        pergunta=pergunta,
        texto_comentario=request.POST['texto_comentario']
    )
    
    comentario.save()

    return HttpResponseRedirect(
        reverse("enquetes:index")
    )