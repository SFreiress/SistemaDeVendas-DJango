from django.shortcuts import render
from .models import Produto, Cliente


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "products/index.html", {"produtos": produtos})


def salvar(request):
    descricaoTS = request.POST.get("descricao")
    precoTS = request.POST.get("preco")
    qtd_estoqueTS = request.POST.get("qtd_estoque")
    Produto.objects.create(descricao=descricaoTS, preco=precoTS, qtd_estoque=qtd_estoqueTS)
    produtos = Produto.objects.all()
    return render(request, "prodcuts/index.html", {"produtos": produtos})


def clients(request):
    clientes = Cliente.objects.all()
    return render(request, "clients/index.html", {"clientes": clientes})



def salvarCliente(request):
    nomeC = request.POST.get("nome")
    rgC = request.POST.get("rg")
    cpfC = request.POST.get("cpf")
    emailC = request.POST.get("email")
    celularC = request.POST.get("celular")
    cepC = request.POST.get("cep")
    enderecoC = request.POST.get("endereco")
    numeroC = request.POST.get("numero")
    complementoC = request.POST.get("complemento")
    bairroC = request.POST.get("bairro")
    cidadeC = request.POST.get("cidade")
    ufC = request.POST.get("uf")
    Cliente.objects.create(nome=nomeC, rg=rgC, cpf=cpfC, email=emailC, celular=celularC, cep=cepC, 
                           endereco=enderecoC, numero=numeroC, complemento=complementoC,bairro=bairroC,
                           cidade=cidadeC,uf=ufC)
    clientes = Cliente.objects.all()
    return render(request, "clients/index.html", {"clientes": clientes})