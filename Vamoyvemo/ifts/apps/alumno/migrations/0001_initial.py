# Generated by Django 5.1 on 2024-10-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateField()),
                ('estado_academico', models.BooleanField()),
            ],
        ),
    ]
