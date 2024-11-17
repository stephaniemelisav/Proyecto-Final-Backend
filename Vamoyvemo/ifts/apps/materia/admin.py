from django.contrib import admin
<<<<<<< HEAD
from apps.materia.models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'codigo')

=======

from apps.materia.models import Materia, MateriaProfesor

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
  list_display = ['codigo', 'nombre', 'descripcion']
>>>>>>> origin/Dev_final
