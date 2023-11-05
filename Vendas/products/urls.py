from products.views import home, salvar
from django.urls import path

app_name = "products"
 
urlpatterns = [
    path("", home, name="home"),
    path("salvar/", salvar, name="salvar"),
]
