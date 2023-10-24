from django.shortcuts import render
from .models import Produto


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})


def salvar(request):
    descricaoTS = request.POST.get("descricao")
    precoTS = request.POST.get("preco")
    qtd_estoqueTS = request.POST.get("qtd_estoque")
    print("desc", descricaoTS)
    print("prec", precoTS)
    print("qtd", qtd_estoqueTS)
    Produto.objects.create(descricao=descricaoTS, preco=precoTS, qtd_estoque=qtd_estoqueTS)
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})
