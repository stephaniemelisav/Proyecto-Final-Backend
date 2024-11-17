from django.db import models

class Cursada(models.Model):
  alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE, related_name='cursadas')
  ciclo_lectivo = models.ForeignKey('cicloLectivo.CicloLectivo', on_delete=models.CASCADE, related_name='cursadas')
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='cursadas')

  estado = models.BooleanField()
  fecha_inscripcion = models.DateField()

def __str__(self):
  return f"{self.alumno}, {self.ciclo_lectivo}, {self.materia}, {self.estado}, {self.fecha_inscripcion}"
