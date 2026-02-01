from django.db import models

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre