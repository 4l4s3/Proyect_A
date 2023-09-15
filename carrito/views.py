from django.shortcuts import render,redirect
from .carrito import Carrito
from AirDc.models import Producto

# Create your views here.

def agregar_producto(request,producto_id):
    
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
    
    return redirect("venta")


def eliminar_producto(request,producto_id):
        
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    
    return redirect("venta")


def restar_producto(request,producto_id):
        
    carro = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carro.restar(producto=producto)
    
    return redirect("venta")


def limpiar_producto(request,producto_id):
        
    carro = Carrito(request)
    carro.limpiar()
    
    return redirect("venta")