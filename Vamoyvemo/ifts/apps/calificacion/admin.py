from django.contrib import admin
from  apps.calificacion.models import Calificacion
# Register your models here.

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('valor', 'comentarios', 'fecha_calificacion')