from django.shortcuts import redirect, render

from .models import Produto


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "products.html", {"produtos": produtos})

def salvar(request):
    if request.method == 'POST':
        Produto.objects.create(
            descricao=request.POST.get("descricao"),
            preco=request.POST.get("preco"),
            qtd_estoque=request.POST.get("qtd_estoque")
        )
        return redirect('products:home')
    
    produtos = Produto.objects.all()
    return render(request, "products.html", {"produtos": produtos})
