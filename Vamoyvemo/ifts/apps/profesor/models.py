from django.db import models

# Create your models here.
class Profesor(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=100)

def __str__(self):
    return f"{self.nombre} {self.especialidad}"
=======
    legajo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(20)

def __str__(self):
    return f"{self.legajo} {self.nombre} {self.apellido} {self.email} {self.telefono}"
>>>>>>> origin/Dev_final
    