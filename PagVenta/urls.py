from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.index),
    path('index', views.index),
    path('articulos_geeks',views.articulos_geek),
    path('juegos_mesa',views.juegos_mesa),
    path('formulario',views.formulario),
    path('agregarProducto',views.inscribir_producto),
    path('eliminarProducto/<int:producto_id>',views.borrar_producto),
    path('editarProducto/<int:producto_id>',views.editar_producto),
    path('listarProductos',views.listar_producto),
    path('listarProductos/<str:producto_tipo>',views.listar_tipo),
]
