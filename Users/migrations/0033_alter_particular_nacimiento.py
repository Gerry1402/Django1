# Generated by Django 5.0.6 on 2024-06-24 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0032_particular_password1_particular_password2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 24, 9, 13, 0, 367584, tzinfo=datetime.timezone.utc), verbose_name='F. de Nacimiento'),
        ),
    ]
