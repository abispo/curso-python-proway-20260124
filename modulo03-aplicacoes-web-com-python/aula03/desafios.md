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
6) Criar um formulário na página de resultados da pergunta. Esse formulário irá conter uma `textarea` e um botão de submit. O usuário poderá deixar um comentário sobre a enquete que ele acabou de responder. Abaixo desse formulário haverá uma lista dos comentários dessa enquete se algum comentário tiver sido feito. O que você deve fazer:

* Criar uma model que irá representar a tabela com os comentários (model `Comentario` e tabela `comentarios`). Essa model terá uma relação N:1 com Pergunta (Uma pergunta pode ter vários comentários, porém 1 comentário está associado a apenas 1 pergunta).
* Gerar e aplicar a migration para a criação dessa tabela.
* Criar uma função view que receberá os dados desse formulário de comentários e irá salvar na tabela `comentarios`. E também criar a rota que irá chamar essa função.
* Alterar o template `resultados.html` para incluir o novo formulário e a listagem de comentários.
* Após o comentário ser salvo, redirecionar o usuário para a página principal do pacote enquetes.