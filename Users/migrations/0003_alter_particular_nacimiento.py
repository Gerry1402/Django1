# Generated by Django 5.0.6 on 2024-06-19 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_particular_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 19, 10, 34, 39, 889286, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
    ]
