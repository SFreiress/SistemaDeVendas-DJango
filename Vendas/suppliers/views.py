from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fornecedor

@login_required(login_url="/login/")
def home(request):
    fornecedores=Fornecedor.objects.all()
    return render(request, "list_supplier.html", {"fornecedores": fornecedores})

@login_required(login_url="/login/")
def create(request):
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
            uf=request.POST.get("uf")
        )
        return redirect('suppliers:home')
    
    return render(request, "create_supplier.html")

@login_required(login_url="/login/")
def edit(request, id):
    fornecedor=get_object_or_404(Fornecedor, id=id)

    if request.method == 'POST':
        fornecedor.nome=request.POST.get("nome")
        fornecedor.cnpj=request.POST.get("cnpj")
        fornecedor.email=request.POST.get("email")
        fornecedor.telefone=request.POST.get("telefone")
        fornecedor.celular=request.POST.get("celular")
        fornecedor.cep=request.POST.get("cep")
        fornecedor.endereco=request.POST.get("endereco")
        fornecedor.numero=request.POST.get("numero")
        fornecedor.complemento=request.POST.get("complemento")
        fornecedor.bairro=request.POST.get("bairro")
        fornecedor.cidade=request.POST.get("cidade")
        fornecedor.uf=request.POST.get("uf")
        fornecedor.save()
        return redirect('suppliers:home')
    
    return render(request, "edit_supplier.html", {"fornecedor": fornecedor})
