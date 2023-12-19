from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_datos/', procesar_formulario, name='contacto_datos'),
    path('perfil/', perfil, name = 'perfil'),
    path('perfil_publico/', perfilPublico, name = 'perfil_publico'),
    path('datos/', datos, name = 'datos'),
    path('datos_default/', datos_default, name = 'datos_default'),
    path('guardar_datos/', guardar_datos, name = 'guardar_datos'),
]