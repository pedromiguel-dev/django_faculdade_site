from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


def utc_ten_days_future():
    return datetime.utcnow() + timedelta(days=10)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        FUNCIONARIO = "FUNCIONARIO", 'Funcionário'
        CLIENTE = "CLIENTE", 'Client'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class FuncionarioManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.FUNCIONARIO)


class Funcionario(User):
    base_role = User.Role.FUNCIONARIO

    funcionario = FuncionarioManager()

    class Meta:
        proxy = True


class ClienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENTE)


class Cliente(User):
    base_role = User.Role.CLIENTE

    cliente = ClienteManager()

    class Meta:
        proxy = True


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to="categoria")

    def __str__(self):
        return self.nome


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length=150)
    precoLavagem = models.FloatField(default=30)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categoria"
    )
    imagem = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nome


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
