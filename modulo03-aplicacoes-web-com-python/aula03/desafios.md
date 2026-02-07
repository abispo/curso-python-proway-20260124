# Desafio

Criar um novo app chamado estatísticas (`python manage.py startapp estatisticas`). Esse app servirá para exibir algumas estatísticas do sistema de enquetes.

Existirá apenas 1 rota (index), que será uma página HTML básica que mostrará uma lista com as seguintes informações:

1) Quantas perguntas estão cadastradas no sistema
2) A média de opções por pergunta
3) Lista das 5 opções com mais votos, mostrando a qual pergunta essa opção pertence. Por exemplo:

| Opção           | Qtd de votos            | Pergunta
| --------------- | ----------------------- | ---------------------------
| Churrasco       | 10                      | Qual a sua comida favorita?
| Sushi           | 5                       | Qual a sua comida favorita?
| Blumenau        | 4                       | Qual a sua cidade

4) Lista das 3 perguntas com mais votos
5) Lista das 3 perguntas com menos votos
