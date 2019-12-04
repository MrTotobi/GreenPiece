"""GreenPiece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('PagVenta.urls')),
    path('index',include('PagVenta.urls')),
    path('articulos_geeks',include('PagVenta.urls')),
    path('juegos_mesa',include('PagVenta.urls')),
    path('formularios',include('PagVenta.urls')),
    path('formularios/<int:formulario_tipo>',include('PagVenta.urls')),
    path('inscribir_formulario',include('PagVenta.urls')),
    path('borrar_formulario/<int:form_id>',include('PagVenta.urls')),
    path('editar_formulario/<int:form_id>',include('PagVenta.urls')),
    path('agregarProducto',include('PagVenta.urls')),
    path('editarProducto/<int:producto_id>',include('PagVenta.urls')),
    path('eliminarProducto/<int:producto_id>',include('PagVenta.urls')),
    path('listarProductos',include('PagVenta.urls')),
    path('listarProductos/<str:producto_tipo>',include('PagVenta.urls'))
]

