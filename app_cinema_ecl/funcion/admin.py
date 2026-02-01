from django.contrib import admin
from .models import Funcion

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'estado')
    list_filter = ('estado', 'fecha_hora')
    search_fields = ('estado',)