from django.contrib import admin
<<<<<<< HEAD
=======

>>>>>>> origin/Dev_final
from  apps.alumno.models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('nombre', 'matricula', 'fecha_ingreso', 'estado_academico')
=======
    list_display = ['nombre', 'apellido', 'email']
>>>>>>> origin/Dev_final
