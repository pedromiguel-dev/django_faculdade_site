from django.db import models


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to="categoria")

    def __str__(self):
        return self.nome
