from django.contrib import admin
from apps.institucion.models  import Institucion

# Register your models here.
@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
  list_display = ('nombre',)