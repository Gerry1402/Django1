# Generated by Django 5.0.6 on 2024-06-21 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_delete_empresa_delete_ong_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='particular',
            name='contrasena',
            field=models.CharField(default='12345678aA', max_length=31, unique=True, verbose_name='Contraseña'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='particular',
            name='contrasena_2',
            field=models.CharField(default='12345678aA', max_length=31, unique=True, verbose_name='Confirmar contraseña'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 21, 13, 6, 52, 482206, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
    ]
