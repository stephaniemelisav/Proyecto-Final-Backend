from django.db import models

class NotificacionEstudiante(models.Model):
  evento = models.ForeignKey('evento.Evento', on_delete=models.CASCADE, related_name='notificacionesEstudiantes')
  alumno = models.ForeignKey('alumno.Alumno', on_delete=models.CASCADE, related_name='notificacionesEstudiantes')
  leido = models.BooleanField(default=False)
  calificacion = models.IntegerField()

  def __str__(self):
    return f"{self.evento} {self.alumno} {self.leido} {self.calificacion}"