from django.contrib import admin
from django.urls import path, include
from .views import *
from paciente import views

urlpatterns = [
    path('', Interfaz.as_view(), name = 'interfaz'),
    path('datos_paciente/<int:pk>/', datos_paciente, name='datos_paciente'),
    path('perfil/', PerfilPsicologoView.as_view(), name = 'perfil-psicologo'),
    path('nuevo', NuevoPsicologo.as_view(), name='nuevo_psicologo'),
    path('guardar-personales/<int:pk>/', guardar_notas_personales, name='guardar_notas_personales'),
    path('guardar_compartidas/<int:pk>/', guardar_notas_compartidas, name='guardar_notas_compartidas'),
    
]