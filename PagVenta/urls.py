from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [   
    path('', views.index),
    path('index', views.index),
    path('articulos_geeks',views.articulos_geek),
    path('juegos_mesa',views.juegos_mesa),
    path('formularios',views.formularios),
    path('inscribir_formulario',views.inscribir_formulario),
    path('editar_formulario/<int:form_id>',views.editar_formulario),
    path('borrar_formulario/<int:form_id>',views.borrar_formulario),
    path('agregarProducto',views.inscribir_producto),
    path('eliminarProducto/<int:producto_id>',views.borrar_producto),
    path('editarProducto/<int:producto_id>',views.editar_producto),
    path('listarProductos',views.listar_producto),
    path('listarProductos/<str:producto_tipo>',views.listar_tipo),
]
