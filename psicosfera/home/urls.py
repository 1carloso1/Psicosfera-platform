from django.urls import path
from .views import *
from paciente.views import actualizar_paciente
from psicologo.views import actualizar_psicologo, actualizar_consultorio, obtener_citas_publico
urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('contacto/', contacto, name='contacto'),
    path('perfil/', perfil, name = 'perfil'),
    path('actualizacion_exitosa/', exito_actualizacion, name = 'actualizacion_exitosa'),
    path('perfil/<str:username>/', perfilPublico, name = 'ver_perfil'),
    path('perfil/<str:username>/agregar-contacto/', agregar_contacto, name='agregar_contacto'),
    path('perfil/<str:username>/enviar-solicitud/', enviar_solicitud, name='enviar_solicitud'),
    path('perfil/<str:username>/eliminar-solicitud/', eliminar_solicitud, name='eliminar_solicitud'),
    path('perfil/<str:username>/eliminar-contacto/', eliminar_contacto, name='eliminar_contacto'),
    path('obtener_citas_publico/<str:username>/', obtener_citas_publico, name='obtener_citas_publico'),
    path('agendar_cita/<str:username>/', agendar_cita, name='agendar_cita'),
    path('datos/', datos, name = 'datos'),
    path('datos_default/', datos_default, name = 'datos_default'),
    path('actualizar_psicologo/', actualizar_psicologo, name = 'actualizar_psicologo'),
    path('actualizar_consultorio/', actualizar_consultorio, name = 'actualizar_consultorio'),
    path('actualizar_paciente/', actualizar_paciente, name = 'actualizar_paciente'),
    path('actualizar_password/', actualizar_password, name = 'actualizar_password'),
    path('enviar_correo_confirmacion/', enviar_correo_confirmacion, name='enviar_correo_confirmacion'),
    path('confirmar_correo/<int:pk>/<str:token>/', confirmar_correo, name='confirmar_correo'),
    path('ajuste_notificaciones/', ajuste_notificaciones, name='ajuste_notificaciones'),
    path('marcar_notificacion_leida/', marcar_notificacion_leida, name='marcar_notificacion_leida'),
]# urls.py
