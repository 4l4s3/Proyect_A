from django.shortcuts import render,redirect
from .carrito import Carrito
from AirDc.models import Producto
from django.contrib import messages

# Create your views here.

def agregar_producto(request,producto_id):
    
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
    messages.success(request, "El producto ha sido agregado al carrito")
    return redirect("/venta/0")


def eliminar_producto(request,producto_id):
        
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    return redirect("/venta/0")



def restar_producto(request,producto_id):
        
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    messages.success(request, "El producto ha sido eliminado del carrito")
    carro.restar(producto=producto)
    
    return redirect("/venta/0")



def limpiar_producto(request):
        
    carro = Carrito(request)
    carro.limpiar()
    
    return redirect("/venta/0")
