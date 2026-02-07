from django.db.models import Count, Avg
from django.shortcuts import render

from enquetes.models import Opcao, Pergunta

def index(request):

    # A chamada Pergunta.objects.count() corresponde ao comando SQL SELECT COUNT(id) FROM perguntas
    qtd_perguntas_cadastradas = Pergunta.objects.count()
    
    # Abaixo chamamos o método all() que irá trazer todos os registros da tabela de opções como uma lista de objetos. Depois contamos a quantidade de registros utilizando a função built-in len()
    # Apesar de funcionar, não é recomendável trazer todos os registros da tabela de uma vez só, por questões de performance da aplicação.
    # qtd_opcoes_cadastradas = len(Opcao.objects.all())
    # qtd_media_de_opcoes_por_perguntas = qtd_opcoes_cadastradas / qtd_perguntas_cadastradas

    # Cálculo da média de opções por pergunta utilizando as chamadas do ORM do Django (annotate, aggregate)

    # O annotate cria um campo em tempo de execução, que será adicionado a cada item da lista
    contagem_opcoes = Pergunta.objects.annotate(
        numero_de_opcoes=Count("opcao")
    )

    # O método aggregate chama uma função de agregação em cima do campo que foi criado com o annotate.
    qtd_media_de_opcoes_por_perguntas = contagem_opcoes.aggregate(
        media_opcoes=Avg("numero_de_opcoes")
    )['media_opcoes']

    lista_opcoes_mais_votadas = Opcao.objects.order_by("-votos")[:5]

    contexto = {
        "qtd_perguntas_cadastradas": qtd_perguntas_cadastradas,
        "qtd_media_de_opcoes_por_perguntas": qtd_media_de_opcoes_por_perguntas,
        "lista_opcoes_mais_votadas": lista_opcoes_mais_votadas
    }

    return render(
        request,
        "estatisticas/index.html",
        context=contexto
    )