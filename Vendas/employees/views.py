from django.shortcuts import redirect, render, get_object_or_404
from .models import Funcionario
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "employees.html", {"funcionarios": funcionarios})

@login_required(login_url="/login/")
def salvar(request):
    if request.method == 'POST':
        Funcionario.objects.create(
            nome=request.POST.get("nome"),
            rg=request.POST.get("rg"),
            cpf=request.POST.get("cpf"),
            email=request.POST.get("email"),
            senha=request.POST.get("senha"),
            cargo=request.POST.get("cargo"),
            nivel_acesso=request.POST.get("nivel_acesso"),
            celular=request.POST.get("celular"),
            cep=request.POST.get("cep"),
            endereco=request.POST.get("endereco"),
            numero=request.POST.get("numero"),
            complemento=request.POST.get("complemento"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
        )
        return redirect('employees:home')
    return render(request, "registerEmployee.html")

@login_required(login_url="/login/")
def atualizar(request, id):
    if request.method == 'POST':
        funcionario = get_object_or_404(Funcionario, id=id)
        funcionario.nome=request.POST.get("nome")
        # funcionario.rg=request.POST.get("rg")
        funcionario.cpf=request.POST.get("cpf")
        funcionario.email=request.POST.get("email")
        # funcionario.senha=request.POST.get("senha")
        # funcionario.cargo=request.POST.get("cargo")
        # funcionario.nivel_acesso=request.POST.get("nivel_acesso")
        funcionario.celular=request.POST.get("celular")
        funcionario.cep=request.POST.get("cep")
        funcionario.endereco=request.POST.get("endereco")
        funcionario.numero=request.POST.get("numero")
        funcionario.complemento=request.POST.get("complemento")
        funcionario.bairro=request.POST.get("bairro")
        funcionario.cidade=request.POST.get("cidade")
        
        funcionario.save()
        return redirect('employees:home')
    
    funcionarios = Funcionario.objects.get(id=id)
    return render(request, "updateEmployee.html", {"funcionario": funcionarios})
