# Generated by Django 4.0.5 on 2023-01-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=33)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=33)),
                ('roll', models.CharField(max_length=33)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
    ]
