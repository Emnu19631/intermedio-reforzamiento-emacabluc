from django.contrib import admin
from .models import Entrada, SnackCompra

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('funcion', 'asiento', 'vendido')

admin.site.register(SnackCompra)