from django.contrib import admin
from django.urls import path, include
from .views import *
from paciente import views

urlpatterns = [
    path('', PacienteInterfazView.as_view(), name = 'perfil'),
    path('perfil/', PerfilView.as_view(), name = 'perfil-paciente'),
    path('nuevo', views.NuevoPaciente.as_view(), name='nuevo_paciente'),
]