from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from users.models import CustomUser

from .models import Funcionario


@login_required(login_url="/login/")
def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "list_employee.html", {"funcionarios": funcionarios})

@login_required(login_url="/login/")
def create(request):
    new_user = None 

    if request.method == 'POST':
        nome_completo = request.POST.get("nome")
        partes_do_nome = nome_completo.split()
        primeiro_nome = partes_do_nome[0]
        ultimo_nome = partes_do_nome[-1] if len(partes_do_nome) > 1 else ""
        email_exists = CustomUser.objects.filter(email=request.POST.get("email")).exists()
        username_exists = CustomUser.objects.filter(username=nome_completo).exists()

        if request.POST.get("nivelAcesso") == "admin":
            if email_exists:
                messages.error(request, "Email already exists. Please choose a different one.")
                return
            if username_exists:
                messages.error(request, "Username already exists. Please choose a different one.")
                return

            try:
                new_user = CustomUser.objects.create_user(
                    username=nome_completo,
                    first_name=primeiro_nome,
                    last_name=ultimo_nome,
                    password=request.POST.get("password"),
                    email=request.POST.get("email"),
                )
            except Exception as e:
                print(request, f"Erro ao criar usuário: {str(e)}")
        else:
            # Use a default user ID, e.g., 1
            default_user_id = 1
            new_user = CustomUser.objects.get(id=default_user_id)

        Funcionario.objects.create(
            nome=request.POST.get("nome"),
            rg=request.POST.get("rg"),
            cpf=request.POST.get("cpf"),
            email=request.POST.get("email"),
            senha=request.POST.get("password"),
            cargo=request.POST.get("cargo"),
            nivel_acesso=request.POST.get("nivelAcesso"),
            telefone=request.POST.get("telefone"),
            celular=request.POST.get("celular"),
            cep=request.POST.get("cep"),
            endereco=request.POST.get("endereco"),
            numero=request.POST.get("numero"),
            complemento=request.POST.get("complemento"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
            uf=request.POST.get("uf"),
            usuario=new_user,
        )
        return redirect('employees:home')

    return render(request, "create_employee.html")

@login_required(login_url="/login/")
def edit(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)

    if request.method == 'POST':
        user = funcionario.usuario

        new_email = request.POST.get("email")
        new_username = request.POST.get("nome")
        nome_completo = new_username
        partes_do_nome = nome_completo.split()
        primeiro_nome = partes_do_nome[0]
        ultimo_nome = partes_do_nome[-1] if len(partes_do_nome) > 1 else ""

        # Check if the new email and username are the same as the old ones
        if new_email == funcionario.email and new_username == funcionario.nome:
        # No changes, skip validation for existing entries  
            pass
        else:
            email_exists = CustomUser.objects.filter(email=new_email).exclude(username=funcionario.email).exists()
            username_exists = CustomUser.objects.filter(username=new_username).exclude(username=funcionario.nome).exists()

            if request.POST.get("nivelAcesso") == "admin":
                if email_exists:
                    messages.error(request, "Email already exists. Please choose a different one.")
                    return render(request, "edit_employee.html", {"funcionario": funcionario})
                if username_exists:
                    messages.error(request, "Username already exists. Please choose a different one.")
                    return render(request, "edit_employee.html", {"funcionario": funcionario})

        funcionario.nome = new_username
        funcionario.rg = request.POST.get("rg")
        funcionario.cpf = request.POST.get("cpf")
        funcionario.email = new_email
        funcionario.senha = request.POST.get("password")
        funcionario.cargo = request.POST.get("cargo")
        funcionario.nivel_acesso = request.POST.get("nivelAcesso")
        funcionario.telefone = request.POST.get("telefone")
        funcionario.celular = request.POST.get("celular")
        funcionario.cep = request.POST.get("cep")
        funcionario.endereco = request.POST.get("endereco")
        funcionario.numero = request.POST.get("numero")
        funcionario.complemento = request.POST.get("complemento")
        funcionario.bairro = request.POST.get("bairro")
        funcionario.cidade = request.POST.get("cidade")
        funcionario.uf = request.POST.get("uf")
        funcionario.save()

        user.first_name = primeiro_nome
        user.last_name = ultimo_nome
        user.email = new_email
        user.username = new_username
        user.set_password(request.POST.get("password"))
        user.save()

        return redirect('employees:home')

    return render(request, "edit_employee.html", {"funcionario": funcionario})

