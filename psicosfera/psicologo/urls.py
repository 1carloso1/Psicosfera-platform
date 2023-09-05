from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', interfaz_psicologo, name = 'interfaz'),
    path('datos_paciente/', datos_paciente, name='datos_paciente'),
    path('perfil/', perfil_psicologo, name = 'perfil_psicologo'),
    path('guardar-personales', guardar_notas_personales, name='guardar_notas_personales'),
    path('guardar_compartidas', guardar_compartidas, name='guardar_compartidas'),
]