from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PacienteInterfazView.as_view(), name = 'perfil'),
    path('perfil/', PerfilView.as_view(), name = 'perfil-paciente'),
]