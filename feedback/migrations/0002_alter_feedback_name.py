# Generated by Django 4.0.3 on 2022-05-30 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
