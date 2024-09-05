from django.contrib import admin
from  .models import Desarrollador
# Register your models here.

@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
# Register your models here.