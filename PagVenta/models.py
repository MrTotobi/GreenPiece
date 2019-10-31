from django.db import models
from django.utils import timezone
import get

class Producto(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    comentario = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    