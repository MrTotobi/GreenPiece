from django import forms
from .models import Producto,Datos_Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo',
        'nombre',
        'tipo',
        'descripcion',
        'comentario',
         'precio',
         'stock',
         'imagen']

class DatosClienteForm(forms.ModelForm):
    class Meta:
        model = Datos_Cliente
        fields = ['nombre_completo',
        'rut',
        'email',
        'fecha_nacimiento',
        'telefono_contacto',
        'region',
        'comuna',
        'direccion',
        'vivienda']