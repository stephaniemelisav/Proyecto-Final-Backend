from django.contrib import admin
from apps.materia.models import Materia, MateriaProfesor


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'descripcion')

@admin.register(MateriaProfesor)
class ProfesorAdmin(admin.ModelAdmin):
  list_display = ('fecha_asignacion',)
