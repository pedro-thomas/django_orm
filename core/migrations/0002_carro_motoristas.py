# Generated by Django 4.2.5 on 2023-10-02 19:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='motoristas',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
