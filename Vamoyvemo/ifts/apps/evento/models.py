from django.db import models
from django.utils import timezone

class Evento(models.Model):
  profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE, related_name='eventos')
  materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE, related_name='eventos')
  tipo = models.OneToOneField('evento.Tipo', on_delete= models.PROTECT, related_name='eventos')
  estado = models.OneToOneField('evento.Estado', on_delete=models.CASCADE, related_name='eventos')
  titulo = models.CharField(max_length=80)
  descripcion = models.CharField(max_length=255)
  fecha_creacion = models.DateField(default= timezone.now)
  fecha_vencimiento = models.DateField()


  def __str__(self):
    return f"{self.profesor}, {self.materia}, {self.tipo}, {self.titulo}, {self.descripcion}, {self.fecha_creacion}"

# Tabla lookup para tipos de eventos: Trabajo práctico, Examen, Aviso General, Calificación
class Tipo(models.Model):
  nombre = models.CharField(max_length=30)

  def __str__(self):
    return f"{self.nombre}"

# Tabla lookup para estado de evento: activo, archivado, eliminado (soft delete)
class Estado(models.Model):
  nombre= models.CharField(max_length=30)

  def __str__(self):
    return f"{self.nombre}"