from django.db import models
from django.conf import settings


class producto(models.Model):
    id_producto = models.AutoField(primary_key=True, null=False)
    # id_proveedor = models.ForeignKey(proveedor,null=True, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=30)
    descript_producto = models.CharField(max_length=120)
    img_producto = models.ImageField(upload_to="productos",null=True)
    valor_compra = models.IntegerField()
    valor_venta = models.IntegerField()
    activo = models.BooleanField()
    encargado = models.CharField(max_length=30)
    
# Create your models here.
