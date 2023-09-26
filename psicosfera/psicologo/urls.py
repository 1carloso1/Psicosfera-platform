from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', interfaz_psicologo, name = 'interfaz'),
    path('datos_paciente/', datos_paciente, name='datos_paciente'),
    path('datos_psicologo/', datos_psicologo, name='datos_psicologo'),
    path('perfil/', perfil_psicologo, name = 'perfil_psicologo'),
    path('guardar_notas/', guardar_notas, name='guardar_notas'),
    path('guardar_psicologo/', guardar_psicologo, name='guardar_psicologo'),
    path('guardar_cita/', guardar_cita, name='guardar_cita'),
    path('obtener_citas/', obtener_citas, name='obtener_citas'),
    path('eliminar_cita/', eliminar_cita, name='eliminar_cita'),
]