from django.db import models

class Materia(models.Model):
  codigo = models.CharField(max_length=20)
  nombre = models.CharField(max_length=80)
  descripcion = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.codigo} {self.nombre} {self.descripcion}"