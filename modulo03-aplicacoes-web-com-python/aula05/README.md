# Desafios

* Implementar a validação de existência de usuário no pré-registro
    * Quando o usuário realizar o pré-registro, você terá que validar se o e-mail que ele informou já não existe na tabela de usuários do sistema (`auth_user`). Dica: Você vai utilizar a model `django.contrib.auth.models.User` para fazer a pesquisa.
* Implementar as seguintes validações na tela de confirmação de registro (não é necessário salvar nada ainda, apenas faça as validações):
    * Verificar se todos os dados do formulário foram preenchidos
    * Verificar se o nome de usuário informado já não existe na tabela de usuários (coluna `username` da tabela `auth_user`)
    * Verificar se o valor do elemento `senha` é igual ao valor do elemento `confirmar_senha`.