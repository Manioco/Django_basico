from django.urls import path
from . import views # From da pasta que estou import views

urlpatterns = [
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name="cadastrar_pessoa"),
    path('inserir_produto/', views.inserir_produto, name="inserir_produto"),
]