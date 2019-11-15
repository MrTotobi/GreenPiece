from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
#-----importamos nuestras estructuras-------------------
from .models  import Producto
from .forms import ProductoForm


def index(request):
    return render(request,'app/index.html')

def articulos_geek(request):
    return render(request,'app/articulos_geeks.html')

def juegos_mesa(request):
    return render(request,'app/juegos_mesa.html')

def formulario(request):
    return render(request,'app/formulario.html')

#----CREAMOS UNA FUNCIUON PARA AGREGAR CARRERA----

def inscribir_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/addProducto')
    else:
        form = ProductoForm()
        return render(request, "app/ins_carrera.html",{'form':form})

def listar_producto(request):
    Producto = Producto.objects.all()
    return render(request,"app/listar_prducto.html"),{'producto':Producto}

def editar_producto(request, codigo):
    instancia = Producto.objects.get(id=codigo)
    form = ProductoForm(instance=instancia)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance= instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()

    return render(request, "app/editar_producto.html",{'form':form})

def borrar_producto(request, codigo):
    instancia = Producto.objects.get(id=codigo)
    instancia.delete()
    return redirect("/")

    
