from suppliers.views import home, salvar, registerSupplier
from django.urls import path

app_name = "suppliers"

urlpatterns = [
    path("", home, name="home"),
    path("registerSupplier/", registerSupplier, name="registerSupplier"),
    path("salvar/", salvar, name="salvar"),
]
