from django.shortcuts import redirect, render
from .models import Fornecedor


# Create your views here.
def home(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers.html", {"fornecedores": fornecedores})


def salvar(request):
    if request.method == 'POST':
        Fornecedor.objects.create(
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
        return redirect('suppliers:home')
    
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers.html", {"fornecedores": fornecedores})
