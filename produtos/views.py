from django.shortcuts import render
from django.http import HttpResponse


def ver_produto(request):
    return render(request, 'ver_produto.html', {'nome': "Leo"})

def inserir_produto(request):
    return HttpResponse("Inserir produto")

