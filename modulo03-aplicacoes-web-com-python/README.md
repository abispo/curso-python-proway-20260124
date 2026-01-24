# Introdução

Nesse módulo vamos aprender a desenvolver aplicações web com o framework Django. Django é um dos frameworks mais populares de Python para desenvolver esse tipo de aplicação.

Para esse módulo vamos utilizar o [Visual Studio Code](https://code.visualstudio.com/) como editor, assim como suas seguintes extensões:
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
* [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
* [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) (opcional)

## Instalação

Idealmente, vamos criar nossa aplicação django dentro de um virtualenv do Python. Assim que criarmos e instalarmos esse virtualenv, vamos digitar o seguinte comando:

`pip install django`

## Configuração

Depois que o django e suas extensões tiverem sido baixadas e instalação, você terá acesso ao comando `django-admin`, que servirá para criar a estrutura inicial do nosso projeto. O seguinte comando cria o nosso projeto `meusite` dentro da pasta `projeto_enquetes`:

`django-admin startproject meusite projeto_enquetes`

O comando anterior irá criar toda a estrutura inicial do nosso projeto dentro da pasta projeto_enquetes. Essa será a pasta raiz, que nós abriremos no VSCode. Assim que a pasta for aberta no editor, você verá a seguinte estrutura de pastas e arquivos: