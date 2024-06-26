# Generated by Django 5.0.6 on 2024-06-23 17:20

import datetime
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0026_alter_particular_options_alter_particular_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='particular',
            options={'verbose_name': 'Particular', 'verbose_name_plural': 'Particulares'},
        ),
        migrations.AlterModelManagers(
            name='particular',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='particular',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='particular',
            name='username',
        ),
        migrations.AlterField(
            model_name='particular',
            name='email',
            field=models.EmailField(default='', max_length=63, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='particular',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 23, 17, 20, 6, 52902, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, unique=True, verbose_name='Teléfono'),
        ),
    ]
