# Generated by Django 5.0.6 on 2024-06-24 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0030_alter_particular_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 24, 0, 55, 32, 282925, tzinfo=datetime.timezone.utc), verbose_name='Nacimiento'),
        ),
    ]
