from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import producto

class productoAdmin(admin.ModelAdmin):
    list_display = ("id_producto","nombre_producto")

admin.site.register(producto,productoAdmin)
# Register your models here.
