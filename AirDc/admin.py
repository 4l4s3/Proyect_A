from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Producto

class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre_producto",)

admin.site.register(Producto,ProductAdmin)
# Register your models here.
