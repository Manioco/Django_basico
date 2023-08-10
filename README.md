Como começar no Django:

Criar uma pasta onde serão inseridos todos os arquivos.

Na pasta, inicar um venv:

    python -m venv nome_do_venv

    nome_do_venv\Scripts\activate

Para desativar:

    deactivate

Em caso de erro por conta do PowerShell

    temporariamente habilita a execução de scripts

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

    Habilita permanentemente

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

Começando com o django:

    pip install django

    django-admin startproject nome_do_projeto

    python manage.py startapp nome_do_app

Rodar o servidor:

    python manage.py runserver

OBS:

O Django trabalha com a arquitetura MVP (Models Views e Templates)

Models = Arquivos responsaveis pelos bancos de dados

Views = Logica das aplicações

Template = HTML ou JSON ou XML. Parte visual do app

Ao Criar um novo APP

Ir em settings.py e adicionar na lista INSTALLED_APPS

Se ele puder ser acessado por algum cliente, deve ser incluido nas urls.py

Os arquivos estaticos (Static) é onde ficam os templates de página e ...?


Para acessar o 'meu site'.com.br/admin

deve criar o usuario e senha:

python manage.py createsuperuser

ele vai pedir:

nome*

email

senha

senha

confirmação 



rodar para atualizar o banco de dados

python manage.py makemigrations

python manage.py migrate
