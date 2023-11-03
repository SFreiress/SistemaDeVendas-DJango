from clients.views import home, salvar
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
]