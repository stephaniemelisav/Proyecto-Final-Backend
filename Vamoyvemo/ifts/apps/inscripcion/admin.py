from django.contrib import admin
from apps.inscripcion.models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
  list_display = ('fecha_inscripcion', 'estado')