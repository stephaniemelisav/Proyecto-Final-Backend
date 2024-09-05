from django.db import models

# Create your models here.
class Alumno(models.Model):
    descripcion = models.CharField(max_length=255)
    