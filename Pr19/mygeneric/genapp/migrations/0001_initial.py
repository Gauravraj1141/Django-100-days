# Generated by Django 4.0.5 on 2023-01-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('clsname', models.CharField(max_length=44)),
                ('section', models.CharField(max_length=22)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
