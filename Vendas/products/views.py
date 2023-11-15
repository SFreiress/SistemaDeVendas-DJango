from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto


# Create your views here.
@login_required(login_url="/login/")
def home(request):
    produtos = Produto.objects.all()
    return render(request, "list_product.html", {"produtos": produtos})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        Produto.objects.create(
            descricao=request.POST.get("descricao"),
            preco=request.POST.get("preco"),
            qtd_estoque=request.POST.get("qtd_estoque")
        )
        return redirect('products:home')

    return render(request, "create_product.html")

@login_required(login_url="/login/")
def edit(request, id):
    produto = get_object_or_404(Produto, pk=id)
    
    if request.method == 'POST':
        produto.descricao=request.POST.get("descricao")
        produto.preco=request.POST.get("preco")
        produto.qtd_estoque=request.POST.get("qtd_estoque")
        produto.save()
        return redirect('products:home')
    
    return render(request, "edit_product.html", {"produto": produto})
