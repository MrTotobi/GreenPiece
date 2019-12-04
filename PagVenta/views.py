from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
#-----importamos nuestras estructuras-------------------
from .models import Producto,Datos_Cliente
from .forms import ProductoForm,DatosClienteForm
from django.contrib import messages
from .serializers import ProductoSerializer
from rest_framework import generics

class API_objects(generics.ListCreateAPIView):
        queryset = Producto.objects.all()
        serializer_class= ProductoSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset = Producto.objects.all()
        serializer_class= ProductoSerializer

def index(request):
    return render(request,'app/index.html')

def articulos_geek(request):
    return render(request,'app/articulos_geeks.html')

def juegos_mesa(request):
    return render(request,'app/juegos_mesa.html')

def formularios(request):
    formularios = Datos_Cliente.objects.all()
    return render(request,"app/formularios.html",{'formularios': formularios})


def inscribir_formulario(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = DatosClienteForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                messages.success(request, 'Los datos de envio se agregaron correctamente')
                return redirect('/inscribir_formulario')
            else:
                return render(request, 'app/inscribir_formulario.html', {'form': form})
            
        else:
            form = DatosClienteForm()
            return render(request,'app/inscribir_formulario.html',{})
    else:
        return render (request, 'app/error.html')

def editar_formulario (request, form_id):
    user = request.user
    if user.is_authenticated:
        instancia = Datos_Cliente.objects.get(id=form_id)
        form = DatosClienteForm(instance=instancia)

        if request.method == "POST":
            form = DatosClienteForm(request.POST, instance= instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                messages.success(request, 'Los datos se editaron correctamente')
            else:
                messages.error(request, 'Los datos no se editaron correctamente')
        return render(request, "app/editar_formulario.html",{'form':form})
    else:
        return render (request, 'app/error.html')

def borrar_formulario(request, form_id):
    user = request.user
    if user.is_authenticated:
        instancia = Datos_Cliente.objects.get(id=form_id)
        instancia.delete()
        return redirect("/formularios")
    else:
        return render (request, 'app/error.html')


def inscribir_producto(request):
    user = request.user
    if user.has_perm('app.admin'):
        if request.method == "POST":
            form = ProductoForm(request.POST,request.FILES)
            if(form.is_valid):
                model_instance = form.save(commit=False)
                model_instance.save()
                messages.success(request, 'El producto se agrego correctamente')
                return redirect('/agregarProducto')
            else:
                messages.error(request,'El producto no se agrego correctamente')
                return HttpResponseRedirect('app/ins_producto.html')
        else:
            form = ProductoForm()
            return render(request, "app/ins_producto.html",{'form':form})
    else:
        return render (request, 'app/error.html')

def editar_producto (request, producto_id):
    user = request.user
    if user.has_perm('app.admin'):
        instancia = Producto.objects.get(id=producto_id)
        form = ProductoForm(instance=instancia)

        if request.method == "POST":
            form = ProductoForm(request.POST, instance= instancia)
            if form.is_valid():
                instancia= form.save(commit=False)
                instancia.save()
                messages.success(request, 'El producto se edito correctamente')
            else:
                messages.error(request, 'El producto no se edito correctamente')
        return render(request, "app/editar_producto.html",{'form':form})
    else:
        return render (request, 'app/error.html')

def listar_producto(request):
    productos = Producto.objects.all()
    return render(request,"app/listar_productos.html",{'productos': productos})

def listar_tipo(request,producto_tipo):
    productos = Producto.objects.filter(tipo=producto_tipo)
    return render(request,"app/listar_tipo.html",{'productos': productos})


def borrar_producto(request, producto_id):
    user = request.user
    if user.has_perm('app.admin'):
        instancia = Producto.objects.get(id=producto_id)
        instancia.delete()
        return redirect("/listarProductos")
    else:
        return render (request, 'app/error.html')
