from django.urls import path
from .views import *
from paciente.views import actualizar_paciente
from psicologo.views import actualizar_psicologo, actualizar_consultorio
urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_datos/', procesar_formulario, name='contacto_datos'),
    path('perfil/', perfil, name = 'perfil'),
    path('actualizacion_exitosa/', exito_actualizacion, name = 'actualizacion_exitosa'),
    path('perfil/<str:username>/', perfilPublico, name = 'ver_perfil'),
    path('datos/', datos, name = 'datos'),
    path('datos_default/', datos_default, name = 'datos_default'),
    path('actualizar_psicologo/', actualizar_psicologo, name = 'actualizar_psicologo'),
    path('actualizar_consultorio/', actualizar_consultorio, name = 'actualizar_consultorio'),
    path('actualizar_paciente/', actualizar_paciente, name = 'actualizar_paciente'),
    path('actualizar_password/', actualizar_password, name = 'actualizar_password'),
    path('marcar_notificacion_leida/', marcar_notificacion_leida, name='marcar_notificacion_leida'),

]# urls.py
