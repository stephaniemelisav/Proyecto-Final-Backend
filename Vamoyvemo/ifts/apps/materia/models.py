from django.db import models

class Materia(models.Model):
  nombre = models.CharField(max_length=80)
  descripcion = models.CharField(max_length=150)

  def __str__(self):
    return f"{self.nombre} {self.descripcion}"

class MateriaProfesor(models.Model):
  materia = models.ForeignKey("materia.Materia", on_delete=models.CASCADE, related_name="materias")
  profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE, related_name="profesores")
  fecha_asignacion = models.DateField()

  def __str__(self):
    return f"{self.fecha_asignacion}"