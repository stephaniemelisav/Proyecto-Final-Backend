from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    estado_academico = models.BooleanField()

    
    def __str__(self):
        return f"{self.nombre} {self.matricula} {self.fecha_ingreso} {self.estado_academico}"
        