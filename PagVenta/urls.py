from django.urls import path, include
from . import views

urlpatterns = [   
    path('', views.index),
    path('index', views.index),
    path('articulos_geeks',views.articulos_geek),
    path('juegos_mesa',views.juegos_mesa),
]
