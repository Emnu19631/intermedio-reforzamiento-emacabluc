from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    duracion = models.IntegerField(help_text="Duración en minutos")
    clasificacion = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo