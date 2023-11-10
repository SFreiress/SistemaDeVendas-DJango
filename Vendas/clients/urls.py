from clients.views import home, salvar
from django.urls import path

app_name = "clients"

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
]