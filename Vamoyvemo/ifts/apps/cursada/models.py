from django.db import models

class Cursada(models.Model):
<<<<<<< HEAD
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  estado = models.BooleanField(default=False)

def __str__(self):
  return f"{self.fecha_inicio} {self.fecha_fin} {self.estado}"
=======
  alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE, related_name='alumnos')
  ciclo_lectivo = models.ForeignKey('cicloLectivo.CicloLectivo', on_delete=models.CASCADE, related_name='ciclosLectivos')
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='materias')

  estado = models.BooleanField()
  fecha_inscripcion = models.DateField()

def __str__(self):
  return f"{self.alumno}, {self.ciclo_lectivo}, {self.materia}, {self.estado}, {self.fecha_inscripcion}"
>>>>>>> origin/Dev_final
