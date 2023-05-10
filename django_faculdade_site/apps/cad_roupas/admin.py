from django.contrib import admin

from django_faculdade_site.apps.cad_roupas import models

# Register your models here.

admin.site.register(models.CarrinhoItem)
admin.site.register(models.Carrinho)
admin.site.register(models.Roupa)
admin.site.register(models.Categoria)
admin.site.register(models.Pedido)