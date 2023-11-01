from django.urls import path
from .views import home, salvar, clients, salvarCliente

urlpatterns = [
    path("", home),
    path("salvar/", salvar, name="salvar"),
    path("clients/", clients, name="clients"),
    path("salvarCliente/", salvarCliente, name="salvarCliente"),
]
