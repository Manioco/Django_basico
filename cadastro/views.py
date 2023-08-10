from django.shortcuts import render
from django.http import HttpResponse
# from .models import Class


def valida_nome(nome):
    pass


def cadastro(request):
    return render(request, 'cadastro.html')
    # if request.method == "POSt":
      # pass
