# Generated by Django 4.2.1 on 2023-05-05 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cad_roupas', '0004_pedido_usuario_alter_pedido_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_devolucao',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 22, 27, 5, 1589)),
        ),
    ]