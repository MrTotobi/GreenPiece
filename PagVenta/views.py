from django.shortcuts import render

def index(request):
    return render(request,'app/index.html')

def articulos_geek(request):
    return render(request,'app/articulos_geeks.html')

def juegos_mesa(request):
    return render(request,'app/juegos_mesa.html')

