from django.contrib import admin
from  .models import Directivo
# Register your models here.

@admin.register(Directivo)
class DirectivoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

