<<<<<<< HEAD
# Generated by Django 5.1 on 2024-10-22 20:45
=======
# Generated by Django 5.1 on 2024-10-30 01:28
>>>>>>> origin/Dev_final

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
    ]
