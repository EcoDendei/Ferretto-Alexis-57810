# Generated by Django 5.0.6 on 2024-07-20 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcontame', '0004_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='asiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='appcontame.asiento'),
        ),
    ]
