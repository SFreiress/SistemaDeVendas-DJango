from suppliers.views import home, create, edit
from django.urls import path

app_name = "suppliers"

urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("edit/<uuid:id>", edit, name="edit"),
]
