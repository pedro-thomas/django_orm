# Generated by Django 4.2.5 on 2023-10-09 13:44

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carro_motoristas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(on_delete=models.SET(core.models.set_default_montadora), to='core.montadora'),
        ),
    ]
