from django.db import models

class Clima(models.Model):
    ciudad = models.CharField(max_length=50)
    temperatura = models.FloatField()
    descripcion = models.TextField()
    icono = models.CharField(max_length=50)

    def __str__(self):
        return self.ciudad
