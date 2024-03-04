from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, max_length = 100)
    cpf = models.CharField(max_length = 12, unique=True)
    rg = models.CharField(max_length = 9)
    celular = models.CharField(max_length = 14)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome