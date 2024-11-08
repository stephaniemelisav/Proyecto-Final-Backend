from django.db import models

class Cursada(models.Model):
  nombre = models.CharField(max_length= 50)
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  en_curso = models.BooleanField(default=False)
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='cursadas')
  institucion = models.ForeignKey('institucion.Institucion', on_delete=models.CASCADE, related_name='cursadas')

def __str__(self):
  return f"{self.nombre} {self.fecha_inicio} {self.fecha_fin} {self.en_curso} {self.materia} {self.intitucion}"
