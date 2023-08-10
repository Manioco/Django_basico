from django.urls import path
from . import views # From da pasta que estou import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
]