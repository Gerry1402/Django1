# Generated by Django 5.0.6 on 2024-06-19 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_alter_empresa_pais_residencia_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='ONG',
        ),
        migrations.RenameField(
            model_name='particular',
            old_name='USERNAME_FIELD',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='password',
        ),
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 19, 17, 3, 34, 782477, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
    ]
