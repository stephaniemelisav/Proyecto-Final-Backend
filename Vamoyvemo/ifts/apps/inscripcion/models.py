from django.db import models

class Inscripcion(models.Model):
  fecha_inscripcion = models.DateField()
  estado = models.BooleanField()

  def __str__(self):
    return f"{self.fecha_inscripcion} {self.estado}"
