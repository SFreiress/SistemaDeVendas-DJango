from clients.views import home, create, edit
from django.urls import path

app_name = "clients"

urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("edit/<str:id>/", edit, name="edit")
]
