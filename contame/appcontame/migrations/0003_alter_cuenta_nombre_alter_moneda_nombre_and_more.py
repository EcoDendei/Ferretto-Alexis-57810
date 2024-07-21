# Generated by Django 5.0.6 on 2024-07-16 18:26

import appcontame.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcontame', '0002_alter_cuenta_nombre_alter_moneda_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='nombre',
            field=appcontame.models.CapitalizeNameField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='nombre',
            field=appcontame.models.CapitalizeNameField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subcuenta',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]