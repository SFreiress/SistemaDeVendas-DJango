import uuid

from django.db import models

class Cliente(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)  
    uf = models.CharField(max_length=50)