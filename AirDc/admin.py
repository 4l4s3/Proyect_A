from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Producto
from .models import Pedido

class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto",)

admin.site.register(Producto,ProductAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("usuario","fecha_pedido","total","estado")

admin.site.register(Pedido,PedidoAdmin)
# Register your models here.
