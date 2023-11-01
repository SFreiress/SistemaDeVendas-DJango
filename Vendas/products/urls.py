from django.urls import path
from .views import home, salvar

urlpatterns = [
    path("", home),
    path("salvar/", salvar, name="salvar"),
]
