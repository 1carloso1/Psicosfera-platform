from django.contrib import admin
from django.urls import path, include
from .views import *
from paciente.views import datos_paciente
urlpatterns = [
    path('', interfaz_psicologo, name = 'interfaz'),
    path('datos_paciente/', datos_paciente, name='datos_paciente'),
    path('datos_psicologo/', datos_psicologo, name='datos_psicologo'),
    path('guardar_notas/', guardar_notas, name='guardar_notas'),
    path('actualizar_psicologo/', actualizar_psicologo, name='actualizar_psicologo'),
    path('guardar_cita/', guardar_cita, name='guardar_cita'),
    path('obtener_citas/', obtener_citas, name='obtener_citas'),
    path('eliminar_cita/', eliminar_cita, name='eliminar_cita'),
    path('paciente_pdf/', paciente_pdf, name='paciente_pdf'),
]