from django.urls import path
from .views import home, save

urlpatterns = [
    path("", home),
    path("save/", save, name="save"),
]
