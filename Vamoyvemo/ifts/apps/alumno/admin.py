from django.contrib import admin
from  apps.alumno.models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'matricula', 'fecha_ingreso', 'estado_academico')