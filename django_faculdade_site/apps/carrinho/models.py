from datetime import datetime

from django.db import models

from django_faculdade_site.apps.accounts.models import User, utc_ten_days_future
from django_faculdade_site.apps.roupa.models import Roupa


# Create your models here.


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrinho")
    pago = models.BooleanField(default=False)


class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name="carrinho_item"
    )
    roupa = models.ForeignKey(
        Roupa, on_delete=models.CASCADE, related_name="carrinho_item"
    )
    tamanho = models.CharField(max_length=1)
    quantidade = models.IntegerField()
    data_compra = models.CharField(max_length=12, default='00000')

    def get_product_price(self):
        price = [self.roupa.valor]
        return sum(price)


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Pedido", null=True)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="Pedido")
    preco_total = models.FloatField(default=0)
    numero_cliente = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(default=datetime.utcnow)
    data_devolucao = models.DateTimeField(default=utc_ten_days_future())
