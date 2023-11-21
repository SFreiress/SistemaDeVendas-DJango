import uuid

from django.db import models
from users.models import CustomUser


class Funcionario(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    nivel_acesso = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)  
    uf = models.CharField(max_length=50)
    usuario = models.ForeignKey( 
        CustomUser,
        on_delete=models.CASCADE,
        default=1
    )