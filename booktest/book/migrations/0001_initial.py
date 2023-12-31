# Generated by Django 4.2.7 on 2023-11-23 18:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('ISBN', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999)])),
            ],
        ),
    ]
