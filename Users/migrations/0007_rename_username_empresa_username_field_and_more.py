# Generated by Django 5.0.6 on 2024-06-19 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_particular_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
        migrations.RenameField(
            model_name='ong',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
        migrations.RenameField(
            model_name='particular',
            old_name='username',
            new_name='USERNAME_FIELD',
        ),
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 19, 11, 24, 37, 325440, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
    ]
