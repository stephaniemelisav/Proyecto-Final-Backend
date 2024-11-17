from django.contrib import admin

from apps.notificacionEstudiante.models import NotificacionEstudiante

# Register your models here.
@admin.register(NotificacionEstudiante)
class NotificacionEstudianteAdmin(admin.ModelAdmin):
  list_display = ['evento', 'alumno', 'leido', 'calificacion']