from suppliers.views import home, salvar, atualizar
from django.urls import path

app_name = "suppliers"

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
    path("editar-fornecedor/<uuid:id>", atualizar, name="atualizar"),
]
