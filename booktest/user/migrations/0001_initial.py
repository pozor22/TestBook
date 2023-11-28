# Generated by Django 4.2.7 on 2023-11-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('mail', models.EmailField(max_length=70)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]