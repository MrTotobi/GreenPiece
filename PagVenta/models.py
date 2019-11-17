from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Producto(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    tipo = models.TextField(default='')
    descripcion = models.TextField()
    comentario = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'productos'

        permissions = (
            ('admin',_('Es admin')),
            ('cliente',_('Es cliente')),
        )

class Datos_Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField()
    telefono_contacto = models.CharField(max_length=12) 
    region = models.TextField()
    comuna = models.TextField()
    direccion = models.TextField()
    vivienda = models.TextField()

    def __str__(self):
        return self.rut


