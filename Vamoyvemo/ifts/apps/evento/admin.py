from django.contrib import admin
from apps.evento.models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
  list_display = ('descripcion', 'fecha', 'hora')
