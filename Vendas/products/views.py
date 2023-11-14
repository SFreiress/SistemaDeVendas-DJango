from django.shortcuts import redirect, render, get_object_or_404

from .models import Produto


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "products.html", {"produtos": produtos})

def create(request):
    if request.method == 'POST':
        Produto.objects.create(
            descricao=request.POST.get("descricao"),
            preco=request.POST.get("preco"),
            qtd_estoque=request.POST.get("qtd_estoque")
        )
        return redirect('products:home')

    return render(request, "create.html")

def edit(request, id):
    produto = get_object_or_404(Produto, pk=id)
    
    if request.method == 'POST':
        produto.descricao = request.POST.get("descricao")
        produto.preco = request.POST.get("preco")
        produto.qtd_estoque = request.POST.get("qtd_estoque")
        produto.save()
        return redirect('products:home')
    
    return render(request, "edit.html", {"produto": produto})
