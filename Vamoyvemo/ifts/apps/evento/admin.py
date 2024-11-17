from django.contrib import admin

from apps.evento.models import Evento, Tipo, Estado

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
  list_display = ['profesor', 'materia', 'tipo', 'titulo', 'descripcion', 'fecha_creacion', 'fecha_vencimiento']

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
  list_display =['nombre',]

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
  list_display = ['nombre',]