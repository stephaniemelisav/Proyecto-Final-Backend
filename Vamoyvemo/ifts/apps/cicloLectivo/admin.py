from django.contrib import admin

from apps.cicloLectivo.models import CicloLectivo

@admin.register(CicloLectivo)
class CicloLectivoAdmin(admin.ModelAdmin):
  list_display = ['anio', 'periodo', 'fecha_inicio', 'fecha_fin', 'estado']

