from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente

# Create your views here.
@login_required(login_url="/login/")
def home(request):
    clientes=Cliente.objects.all()
    return render(request, "list_client.html", {"clientes": clientes})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nome=request.POST.get("nome"),
            rg=request.POST.get("rg"),
            cpf=request.POST.get("cpf"),
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
        return redirect('clients:home')

    return render(request, "create_client.html")

@login_required(login_url="/login/")
def edit(request, id):
    cliente=get_object_or_404(Cliente, pk=id)
    
    if request.method == 'POST':
        cliente.nome=request.POST.get("nome")
        cliente.rg=request.POST.get("rg")
        cliente.cpf=request.POST.get("cpf")
        cliente.email=request.POST.get("email")
        cliente.telefone=request.POST.get("telefone")
        cliente.celular=request.POST.get("celular")
        cliente.cep=request.POST.get("cep")
        cliente.endereco=request.POST.get("endereco")
        cliente.numero=request.POST.get("numero")
        cliente.complemento=request.POST.get("complemento")
        cliente.bairro=request.POST.get("bairro")
        cliente.cidade=request.POST.get("cidade")
        cliente.uf=request.POST.get("uf")
        cliente.save()
        return redirect('clients:home')

    return render(request, "edit_client.html", {"cliente": cliente})