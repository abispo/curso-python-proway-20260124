from django.shortcuts import render
from django.http import HttpResponse

from .models import Pergunta

def index(request):
    ultimas_cinco_perguntas = Pergunta.objects.order_by(
        "-data_publicacao"
    )[:5]

    perguntas = [p.texto_pergunta for p in ultimas_cinco_perguntas]

    saida = ", ".join(perguntas)
    return HttpResponse(saida)

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está nos detalhes da pergunta {pergunta_id}")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está na página de resultados da pergunta {pergunta_id}")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}")