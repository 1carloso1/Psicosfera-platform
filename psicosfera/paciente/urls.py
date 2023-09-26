from django.contrib import admin
from django.urls import path, include
from .views import *
from paciente import views

urlpatterns = [
    path('', PacienteInterfazView.as_view(), name = 'paciente'),
    path('perfil/', PerfilView.as_view(), name = 'perfil-paciente'),
    path('autocompletar-especialidades/', autocompletar_especialidades, name = 'autocompletar-especialidades'),
    path('autocompletar-ubicaciones/', autocompletar_ubicaciones, name = 'autocompletar-ubicaciones'),
    path('filtrar_psicologos/', psicologos_por_especialidad_nombre, name = 'filtrar_psicologos'), 
]