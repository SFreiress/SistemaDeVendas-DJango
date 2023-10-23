from django.shortcuts import render
from .models import Produto


# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})


def salvar(request):
    descricao = request.POST.get("descricao")
    Produto.objects.create(descricao=descricao)
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})
