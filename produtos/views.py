from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


def ver_produto(request):
    if request.method == "GET":
        nome = "Leoanrdo Worm Vieira"
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()

        return HttpResponse(f"POST CHAMADO {nome}, {idade}")

def inserir_produto(request):
    return HttpResponse("Inserir produto")

