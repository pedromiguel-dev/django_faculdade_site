from django.db import models

from django_faculdade_site.apps.categoria.models import Categoria


# Create your models here.

class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length=150)
    precoLavagem = models.FloatField(default=30)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categoria"
    )
    imagem = models.ImageField(upload_to="images")
    quantidade = models.IntegerField(default=10)

    def __str__(self):
        return self.nome
