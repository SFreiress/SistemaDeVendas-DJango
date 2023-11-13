from employees.views import home, salvar
from django.urls import path

app_name = "employees"

urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
]
