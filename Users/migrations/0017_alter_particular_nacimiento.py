# Generated by Django 5.0.6 on 2024-06-21 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_alter_particular_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 21, 16, 7, 21, 422748, tzinfo=datetime.timezone.utc), verbose_name='Fecha nacimiento'),
        ),
    ]
