from django.db import models

class Materia(models.Model):
  nombre = models.CharField(max_length=80)
  codigo = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.nombre} {self.codigo}"
