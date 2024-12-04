from django.contrib import admin

from apps.cicloLectivo.models import CicloLectivo

@admin.register(CicloLectivo)
class CicloLectivoAdmin(admin.ModelAdmin):
  list_display = ['anio', 'periodo', 'fechaInicio', 'fechaFin', 'estado']

