from django.db import models

# Create your models here.
class Alumno(models.Model):
    numeroLegajo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    estado = models.BooleanField()

    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"