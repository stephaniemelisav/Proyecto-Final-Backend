from django.db import models

class Evento(models.Model):
  descripcion = models.CharField(max_length=250)
  fecha = models.DateField()
  hora = models.TimeField()

  def __str__(self):
    return f"{self.descripcion} {self.fecha}  {self.hora}"