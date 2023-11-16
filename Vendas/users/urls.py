from django.urls import path
from users.views import login_user, logout_user

app_name = 'users'

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout_user'),
]