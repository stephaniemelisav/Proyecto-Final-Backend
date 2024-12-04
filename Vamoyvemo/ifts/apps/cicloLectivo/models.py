from django.db import models

class CicloLectivo(models.Model):
  anio = models.IntegerField()
  periodo = models.CharField(max_length=50)
  fechaInicio = models.DateField()
  fechaFin = models.DateField()
  estado = models.BooleanField()

  def __str__(self):
    return f"{self.anio} {self.periodo} {self.fechaInicio} {self.fechaFin} {self.estado}"