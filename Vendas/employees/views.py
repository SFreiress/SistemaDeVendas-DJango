from django.shortcuts import redirect, render, get_object_or_404
from .models import Funcionario
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    funcionarios=Funcionario.objects.all()
    return render(request, "list_employee.html", {"funcionarios": funcionarios})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
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
        )
        return redirect('employees:home')

    return render(request, "create_employee.html")

@login_required(login_url="/login/")
def edit(request, id):
    funcionario=get_object_or_404(Funcionario, id=id)

    if request.method == 'POST':
        funcionario.nome=request.POST.get("nome")
        funcionario.rg=request.POST.get("rg")
        funcionario.cpf=request.POST.get("cpf")
        funcionario.email=request.POST.get("email")
        funcionario.senha=request.POST.get("password")
        funcionario.cargo=request.POST.get("cargo")
        funcionario.nivel_acesso=request.POST.get("nivelAcesso")
        funcionario.telefone=request.POST.get("telefone")
        funcionario.celular=request.POST.get("celular")
        funcionario.cep=request.POST.get("cep")
        funcionario.endereco=request.POST.get("endereco")
        funcionario.numero=request.POST.get("numero")
        funcionario.complemento=request.POST.get("complemento")
        funcionario.bairro=request.POST.get("bairro")
        funcionario.cidade=request.POST.get("cidade")
        funcionario.save()
        return redirect('employees:home')

    return render(request, "edit_employee.html", {"funcionario": funcionario})
