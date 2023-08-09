from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Interfaz.as_view(), name = 'interfaz'),
    path('perfil/', PerfilPsicologoView.as_view(), name = 'perfil-psicologo'),
    
]