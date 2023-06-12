from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('otra/',views.otra, name='otra'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
]