from django.shortcuts import redirect, render
from .models import Cliente


# Create your views here.
def home(request):
    clientes = Cliente.objects.all()
    return render(request, "clients.html", {"clientes": clientes})


def salvar(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nome=request.POST.get("nome"),
            rg=request.POST.get("rg"),
            cpf=request.POST.get("cpf"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            cep=request.POST.get("cep"),
            endereco=request.POST.get("endereco"),
            numero=request.POST.get("numero"),
            complemento=request.POST.get("complemento"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
        )
        return redirect('clients:home')
    
    clientes = Cliente.objects.all()
    return render(request, "clients.html", {"clientes": clientes})
