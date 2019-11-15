from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

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
        db_table = 'productos'

        permissions = (
            ('admin',_('Es admin')),
            ('cliente',_('Es cliente')),
        )

class Datos_Cliente(models.Model):
    Nombre_Completo = models.CharField(max_length=100)
    Rut = models.CharField(max_length=10)
    Email = models.CharField(max_length=70)
    Fecha_de_Nacimiento = models.DateField()
    Telefono_de_Contacto = models.CharField(max_length=12) 
    Region = models.TextField()
    Comuna = models.TextField()
    Vivienda = models.TextField()

    def __str__(self):
        return self.nombre


