from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
#-----importamos nuestras estructuras-------------------
from .models import Producto
from .forms import ProductoForm,DatosClienteForm
from django.contrib import messages



def index(request):
    return render(request,'app/index.html')

def articulos_geek(request):
    return render(request,'app/articulos_geeks.html')

def juegos_mesa(request):
    return render(request,'app/juegos_mesa.html')

def formulario(request):
    if request.method == 'POST':
        form = DatosClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            messages.success(request, 'Los datos de envio se agregaron correctamente')
            return redirect('/formulario')
        else:
            return render(request, 'app/formulario.html', {'form': form})
            
    else:
        form = DatosClienteForm()
        return render(request,'app/formulario.html',{})


def inscribir_producto(request):
    user = request.user
    if user.has_perm('app.admin'):
        if request.method == "POST":
            form = ProductoForm(request.POST)
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
