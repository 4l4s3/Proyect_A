from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('otra/',views.otra, name='otra'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('', views.index2, name='index2'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('venta/', views.venta, name='venta'),
    path('verification/', include('verify_email.urls')),
]