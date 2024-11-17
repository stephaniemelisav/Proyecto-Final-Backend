from django.db import models

class Cursada(models.Model):
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  estado = models.BooleanField(default=False)

def __str__(self):
  return f"{self.fecha_inicio} {self.fecha_fin} {self.estado}"
