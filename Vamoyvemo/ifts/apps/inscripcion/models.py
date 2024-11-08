from django.db import models

class Inscripcion(models.Model):
  fecha_inscripcion = models.DateField()
  estado = models.BooleanField()
  cursada = models.OneToOneField('cursada.Cursada', on_delete=models.CASCADE, related_name='inscripciones', default=None)

  def __str__(self):
    return f"{self.fecha_inscripcion} {self.estado} {self.cursada}"
