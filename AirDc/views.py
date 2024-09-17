from decimal import Decimal
from django.utils import timezone
from datetime import timedelta,datetime
import os
import random
from django.urls import reverse
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from Administración import urls
from carrito.context_processor import importe_total_carrito
from .forms import crearFormUsuario
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import crearFormUsuario,formProducto
from verify_email.email_handler import send_verification_email
from .models import Producto
from rest_framework import viewsets
from .serializer import productos_serializer
from django.contrib import messages
from django.shortcuts import render
from .models import Pedido
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests
# Create your views here.
iconF = '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">
  <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
  </svg>'''
iconI = '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
  <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
</svg>'''
iconU = '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
  <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
</svg>'''

def about(request):
  return render(request, 'about.html',{
        'iconI': mark_safe(iconI),
        'iconF':mark_safe(iconF),
        'iconU':mark_safe(iconU),
  })



def contact(request):
  if request.method == 'POST':
    
   asunto = request.POST['asunto']
   mensaje = "Mensaje:" + request.POST['mensaje'] +"  " + "Teléfono: " + request.POST['telefono'] +"  "+ "Email: " + request.POST['email'] 
   email = settings.EMAIL_HOST_USER
   recipiente = ["us.airdc@gmail.com"]
   send_mail(asunto,mensaje,email,recipiente)
   
   messages.success(request, "El mensaje ha sido enviado")
  return render(request, 'contact.html',{
        'iconI': mark_safe(iconI),
        'iconF':mark_safe(iconF),
        'iconU':mark_safe(iconU),
  })
  
def formProduct(request,id=None):
  product = Producto.objects.all()
  if request.method == 'POST':
    form = formProducto(request.POST,request.FILES)
    if form.is_valid():
       form.save()
  elif request.method == 'GET':
    if id == 0:
      product = Producto.objects.all()
      form = formProducto() 
    else:
     product = Producto.objects.filter(id=id)
     form = formProducto()
    if(product.exists()):
       product1 = product.first().id
      
  else:
    form = formProducto()
  return render(request,'formProducto.html',{
    # 'product1': product1,
    'form':form,
    'iconI': mark_safe(iconI),
    'iconF':mark_safe(iconF),
    'iconU':mark_safe(iconU),
    'producto': product
  })
     
         
def index(request):
  product = Producto.objects.all()
  return render(request, 'index.html', {
        'Producto': product,
        'iconI': mark_safe(iconI),
        'iconF':mark_safe(iconF),
        'iconU':mark_safe(iconU),

    })
     
     
def iniciar_sesion(request):
  page = 'iniciar'
  form = crearFormUsuario() 
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password1']
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('../')
    
  return render(request,'iniciar_sesion.html',{
        'page': page,
        'form': form
  })
     
     
     
def registrarse(request):
    page = 'registrarse'
    form = crearFormUsuario() 
    if request.method == 'POST':
        # Validar el formulario primero
        form = crearFormUsuario(request.POST)
        if form.is_valid():
            messages.success(request, "El usuario ha sido registrado, revise su correo electrónico para verificarlo.")    
            inactive_user = send_verification_email(request,form)
    return render(request, 'iniciar_sesion.html', {'form': form, 'page': page}) 
  
  
  
def logoutUser(request):
    logout(request)
    return redirect('iniciar')  
  
  
  
def venta(request, id=None, name=None ):
  if request.method == 'POST':
    nombre_producto = request.POST.get('search','')
    product = Producto.objects.filter(nombre_producto__icontains=nombre_producto)
    search = False
    
  elif request.method == 'GET':
    if id == 0:
      product = Producto.objects.all()
      search = False
    else:
     search = True
     product = Producto.objects.filter(id=id)
  # else:
  #   product = Producto.objects.all()
    
  return render(request, 'venta.html', {
        'search': search,
        'iconI': mark_safe(iconI),  # Asegúrate de definir iconI, iconF, iconU antes de usarlos
        'iconF': mark_safe(iconF),
        'iconU': mark_safe(iconU),
        'producto': product
    })


class productos_view(viewsets.ModelViewSet):
  serializer_class = productos_serializer
  queryset = Producto.objects.all()

def historial_pedidos(request):
     if request.user.username == "administrador":
      pedidos = Pedido.objects.filter()
      return render(request, 'historial_pedidos.html', {'pedidos': pedidos})
     else:
       pedidos = Pedido.objects.filter(usuario=request.user)
       return render(request, 'historial_pedidos.html', {'pedidos': pedidos})

def pago_response(request):
    # Obtener el usuario actual (asumiendo que el usuario está autenticado)
    usuario = request.user

    # Obtener el importe total del carrito con manejo de errores
    importe_total = request.session.get('importe_total_carrito')

    if importe_total is None:
        # Manejar el caso en que el valor no está en la sesión
        importe_total = 0.00  # Asignar un valor por defecto

    # Verificar el tipo de dato y convertir si es necesario
    if isinstance(importe_total, set):
        # Si es un conjunto, tomar el primer elemento (si es un número)
        importe_total = float(list(importe_total)[0])
    elif not isinstance(importe_total, (int, float)):
        # Si no es un número, manejar el error
        raise ValueError("El valor de importe_total_carrito no es un número válido")

    # Crear un nuevo pedido
    pedido = Pedido.objects.create(
        usuario=usuario,
        total=importe_total,
        fecha_pedido=timezone.now() + timedelta(hours=0, minutes=0)  # Fecha y hora actual
    )

    # Limpiar el carrito de la sesión
    request.session['carrito'] = {}

    return render(request, 'pago_confirmado.html')