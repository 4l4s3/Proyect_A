from django.urls import path,include
from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
router = routers.DefaultRouter()
router.register(r'productos',views.productos_view, 'productos')

urlpatterns = [
    # path('otra/',views.otra, name='otra'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('logout/',views.logoutUser, name='logout'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('venta/<int:id>/', views.venta, name='venta'),
    path('verification/', include('verify_email.urls')),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar'),
    path('form-producto/<int:id>/', views.formProduct, name='formProducto'),
    path('historial/', views.historial_pedidos, name='historial'),
    path('pago/response/', views.pago_response, name='pago_response'),
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Credential API')),
]