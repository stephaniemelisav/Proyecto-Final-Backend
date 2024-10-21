from django.db import models

class Calificacion(models.Model):
  valor = models.IntegerField(default=0)
  comentarios = models.CharField(max_length=250)
  fecha_calificacion = models.DateField()
  
  def __str__(self):
    return f"{self.valor}"
