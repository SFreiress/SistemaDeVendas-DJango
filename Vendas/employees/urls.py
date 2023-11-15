from employees.views import home, salvar, atualizar
from django.urls import path

app_name = "employees"

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
    path("editar-funcionario/<uuid:id>", atualizar, name="atualizar")
]
