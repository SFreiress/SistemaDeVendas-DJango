from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render
from django.contrib import messages


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