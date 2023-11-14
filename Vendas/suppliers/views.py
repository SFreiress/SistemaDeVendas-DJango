from django.shortcuts import redirect, render, get_object_or_404
from .models import Fornecedor


# Create your views here.
def home(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "suppliers.html", {"fornecedores": fornecedores})

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
    
    return render(request, "registerSupplier.html")

def atualizar(request, id):
    if request.method == 'POST':
        fornecedor = get_object_or_404(Fornecedor, id=id)
        fornecedor.nome = request.POST.get("nome")
        fornecedor.cnpj = request.POST.get("cnpj")
        fornecedor.email = request.POST.get("email")
        fornecedor.telefone = request.POST.get("telefone")
        fornecedor.celular = request.POST.get("celular")
        fornecedor.cep = request.POST.get("cep")
        fornecedor.endereco = request.POST.get("endereco")
        fornecedor.numero = request.POST.get("numero")
        fornecedor.complemento = request.POST.get("complemento")
        fornecedor.bairro = request.POST.get("bairro")
        fornecedor.cidade = request.POST.get("cidade")
        fornecedor.uf = request.POST.get("uf")

        fornecedor.save()
        return redirect('suppliers:home')
    
    supplier = Fornecedor.objects.get(id=id)
    return render(request, "updateSupplier.html", {"fornecedor": supplier})
