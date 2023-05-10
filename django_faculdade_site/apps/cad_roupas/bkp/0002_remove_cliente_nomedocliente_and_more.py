# Generated by Django 4.2.1 on 2023-05-05 13:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cad_roupas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nomeDoCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='senhaDoCliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='imagem',
            field=models.ImageField(default='cat-img.png', upload_to='clientes'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default='Genérica', max_length=250),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carrinhoitem',
            name='data_compra',
            field=models.CharField(default='00000', max_length=12),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_total', models.FloatField(default=0)),
                ('numero_cliente', models.CharField(max_length=20)),
                ('data_pedido', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('data_devolucao', models.DateTimeField(default=datetime.datetime(2023, 5, 15, 13, 19, 55, 992355))),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pedido', to='cad_roupas.carrinho')),
            ],
        ),
    ]