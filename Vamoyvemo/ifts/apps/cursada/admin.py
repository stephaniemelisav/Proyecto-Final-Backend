from django.contrib import admin
<<<<<<< HEAD
=======

>>>>>>> origin/Dev_final
from apps.cursada.models import Cursada

@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
<<<<<<< HEAD
  list_display = ('fecha_inicio', 'fecha_fin', 'estado')
=======
  list_display = ['alumno', 'ciclo_lectivo', 'materia', 'estado', 'fecha_inscripcion']
>>>>>>> origin/Dev_final
