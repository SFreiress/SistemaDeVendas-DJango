from django.shortcuts import redirect, render
from .models import Fornecedor


# Create your views here.
def home(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers.html", {"fornecedores": fornecedores})

def registerSupplier(request):
    return render(request, "registerSupplier.html")


def salvar(request):
    if request.method == 'POST':
        Fornecedor.objects.create(
            nome=request.POST.get("nome"),
            cnpj=request.POST.get("cnpj"),
            email=request.POST.get("email"),
            telefone=request.POST.get("telefone"),
            celular=request.POST.get("celular"),
            cep=request.POST.get("cep"),
            endereco=request.POST.get("endereco"),
            numero=request.POST.get("numero"),
            complemento=request.POST.get("complemento"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
            uf=request.POST.get("uf"),
        )
        return redirect('suppliers:home')
    
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers.html", {"fornecedores": fornecedores})
