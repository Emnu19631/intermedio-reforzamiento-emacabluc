from django.db import models
from pelicula.models import Pelicula

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.fecha_hora}"