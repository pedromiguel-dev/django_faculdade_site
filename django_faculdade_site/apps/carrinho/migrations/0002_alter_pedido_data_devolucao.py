# Generated by Django 4.2.1 on 2023-06-04 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_devolucao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 0, 50, 11, 411626)),
        ),
    ]
