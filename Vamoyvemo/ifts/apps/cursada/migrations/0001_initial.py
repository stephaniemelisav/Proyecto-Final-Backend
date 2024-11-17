# Generated by Django 5.1 on 2024-11-17 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('cicloLectivo', '__first__'),
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('fecha_inscripcion', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='alumno.alumno')),
                ('ciclo_lectivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='cicloLectivo.ciclolectivo')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='materia.materia')),
            ],
        ),
    ]
