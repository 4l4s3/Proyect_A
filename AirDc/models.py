from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    # id_proveedor = models.ForeignKey(proveedor,null=True, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=30)
    descript_producto = models.CharField(max_length=120)
    img_producto = models.ImageField(upload_to="productos",null=True)
    valor_compra = models.IntegerField()
    precio_producto = models.IntegerField()
    activo = models.BooleanField()
    
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    # Campos adicionales para productos, estado, etc.
    productos = models.ManyToManyField('Producto') # Asumiendo un modelo Producto
    estado = models.CharField(max_length=50, default='Pendiente')