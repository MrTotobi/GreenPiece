from django.db import models
from django.utils import timezone

class Producto(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    comentario = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
            ('admin',('Es admin')),
            ('cliente',('Es cliente')),
        )
