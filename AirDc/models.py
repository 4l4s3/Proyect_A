from django.db import models
from django.conf import settings

class Producto(models.Model):
    # id_proveedor = models.ForeignKey(proveedor,null=True, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=30)
    descript_producto = models.CharField(max_length=120)
    img_producto = models.ImageField(upload_to="productos",null=True)
    valor_compra = models.IntegerField()
    precio_producto = models.IntegerField()
    encargado = models.CharField(max_length=30)
    activo = models.BooleanField()
    
    
    
# Create your models here.
