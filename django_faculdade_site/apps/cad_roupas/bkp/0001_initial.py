# Generated by Django 4.2.1 on 2023-05-04 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
                ('imagem', models.ImageField(upload_to='categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDoCliente', models.CharField(max_length=200)),
                ('senhaDoCliente', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.FloatField(default=0)),
                ('descricao', models.TextField(max_length=150)),
                ('precoLavagem', models.FloatField(default=30)),
                ('imagem', models.ImageField(upload_to='images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='cad_roupas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=1)),
                ('quantidade', models.IntegerField()),
                ('data_compra', models.CharField(max_length=12)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_item', to='cad_roupas.carrinho')),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinho_item', to='cad_roupas.roupa')),
            ],
        ),
    ]