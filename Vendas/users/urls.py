from django.urls import path
from users.views import home

app_name = 'users'

urlpatterns = [
    path('', home, name='login'),
]