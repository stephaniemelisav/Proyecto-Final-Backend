from django.db import models

# Create your models here.
class Alumno(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    estado_academico = models.BooleanField()

    
    def __str__(self):
        return f"{self.nombre} {self.matricula} {self.fecha_ingreso} {self.estado_academico}"
        
=======
    numeroLegajo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    estado = models.BooleanField()

    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
>>>>>>> origin/Dev_final
