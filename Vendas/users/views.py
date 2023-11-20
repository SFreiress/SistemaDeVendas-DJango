from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import CustomUser


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/login/')


def create_newuser(nome_completo, primeiro_nome, ultimo_nome, password, newemail):
    print(newemail)
    if CustomUser.objects.filter(email=newemail).exists():
        return ('Email já existe') 
    if CustomUser.objects.filter(username=nome_completo).exists():
        return ('Usuário já existe')

    CustomUser.objects.create_user(
            email=newemail,
            password=password,
            first_name=primeiro_nome,
            last_name=ultimo_nome,
            username=nome_completo,
        )
    return None
