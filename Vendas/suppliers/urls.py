from suppliers.views import home, salvar
from django.urls import path

app_name = "suppliers"

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
]
