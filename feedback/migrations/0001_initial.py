# Generated by Django 4.0.3 on 2022-05-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=60)),
                ('feedback', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
