from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_datos/', procesar_formulario, name='contacto_datos'),
    path('perfil/', perfil, name = 'perfil'),
    path('perfil/<str:username>/', perfilPublico, name = 'ver_perfil'),
    path('datos/', datos, name = 'datos'),
    path('guardar_datos/', guardar_datos, name = 'guardar_datos'),
]