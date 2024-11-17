from django.contrib import admin

from apps.asignacion.models import Asignacion

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
  list_display = ['profesor', 'materia', 'cicloLectivo']