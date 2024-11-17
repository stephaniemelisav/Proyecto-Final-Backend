from django.contrib import admin
from  .models import Profesor
# Register your models here.

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('legajo', 'nombre', 'apellido', 'email', 'telefono')
