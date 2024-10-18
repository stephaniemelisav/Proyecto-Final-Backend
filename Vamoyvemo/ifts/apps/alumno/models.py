from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    #anios = models.CharField(max_length=50)
    descripcion = models.IntegerField()
    
    def __str__(self):
        return self.nombre
        