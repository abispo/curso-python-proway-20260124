# Desafio

Criar uma estrutura para que o usuário consiga alterar os seus dados de Perfil(nome, data de nascimento, etc). Você terá que fazer o seguinte:

## Criação do pacote `usuarios`

Você irá criar e registrar no projeto o pacote `usuarios`. A url raiz será `usuarios/`.

## Criação da model `Perfil`

Dentro do pacote `usuarios`, você irá criar a model `Perfil`. Essa model irá armazenar as seguintes informações de perfil do usuário:
    * Data de nascimento (tipo `DateField`)
    * Gênero (tipo `CharField`)
    * Endereço (tipo `CharField`)

Essa model terá uma relação de `1:1` (Um-Para-Um) com a model `django.contrib.auth.models.User`. Ao invés de usar a classe `ForeignKey`, você usará a classe `OneToOneField`. Você pode consultar a documentação dessa classe [aqui](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField).

**ATENÇÃO!** Quando criamos/alteramos qualquer model, precisamos gerar as migrations (`python manage.py makemigrations`) e logo em seguida aplicá-las (`python manage.py migrate`).

## Criar a rota de perfil do usuário.
Essa rota servirá para o usuário visualizar e editar as suas informações pessoais. O caminho dessa rota será `eu/`. Ou seja, o caminho completo onde o usuário conseguirá acessar seus dados pessoais será `usuarios/eu/`

## Criar a página de perfil do usuário

Quando o usuário acessar a rota `usuarios/eu/`, a página de perfil será carregada. Essa página consistirá de um formulário com os dados preenchidos nos campos correspondentes. Ou seja, esse formulário terá os seguintes campos:

* Nome de usuário (esse campo não será editável)
* E-mail (esse campo não será editável)
* Nome
* Sobrenome
* Data de Nascimento
* Gênero
* Endereço
* Botão "Enviar"

Como dito anteriormente, caso esses dados estejam preenchidos nas tabelas, eles devem ser carregados nos elementos.

## Criação da lógica de edição das informações

Após o usuário preencher os dados e clicar no botão enviar, você deverá capturar esses dados e salvar nas tabelas correspondentes (`Nome` e `E-mail` na tabela `User` e os demais dados na tabela `Perfil`). Implemente as validações que você achar necessárias.