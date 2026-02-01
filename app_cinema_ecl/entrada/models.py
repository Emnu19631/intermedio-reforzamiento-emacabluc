from django.db import models
from funcion.models import Funcion

class Entrada(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    asiento = models.CharField(max_length=10)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"Asiento {self.asiento} - {self.funcion.pelicula.titulo}"

class SnackCompra(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)