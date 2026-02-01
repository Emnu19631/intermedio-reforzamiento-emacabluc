from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'clasificacion')
    search_fields = ('titulo', 'genero')
    list_filter = ('genero', 'clasificacion')