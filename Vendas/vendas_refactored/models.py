import uuid
from django.db import models


# Create your models here.
class Produto(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.IntegerField()

    def __str__(self) -> str:
        return self.descricao
