# Generated by Django 4.2.1 on 2023-06-04 00:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roupa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_total', models.FloatField(default=0)),
                ('numero_cliente', models.CharField(max_length=20)),
                ('data_pedido', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('data_devolucao', models.DateTimeField(default=datetime.datetime(2023, 6, 14, 0, 49, 39, 449636))),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pedido', to='carrinho.carrinho')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pedido', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=1)),
                ('quantidade', models.IntegerField()),
                ('data_compra', models.CharField(default='00000', max_length=12)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_item', to='carrinho.carrinho')),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_item', to='roupa.roupa')),
            ],
        ),
    ]
