from django.urls import path,include
from . import views

app_name="carrito"

urlpatterns = [
    path("agregar/<int:producto_id>/",views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/",views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/",views.restar_producto, name="restar"),
    path("limpiar/<int:producto_id>/",views.limpiar_producto, name="limpiar"),
]