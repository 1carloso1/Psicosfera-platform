from django.contrib import admin
from django.urls import path, include
from .views import *
from psicologo import views

urlpatterns = [
    path('', Interfaz.as_view(), name = 'interfaz'),
    path('perfil/', PerfilPsicologoView.as_view(), name = 'perfil-psicologo'),
    path('nuevo', views.NuevoPsicologo.as_view(), name='nuevo_psicologo'),
]