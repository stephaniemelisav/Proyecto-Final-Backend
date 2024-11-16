from django.db import models

class CicloLectivo(models):
  anio = models.IntegerField()
  periodo = models.CharField(max_length=50)
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  estado = models.BooleanField()

  def __str__(self):
    return f"{self.anio} {self.periodo} {self.fecha_inicio} {self.fecha_fin} {self.estado}"