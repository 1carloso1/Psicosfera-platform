from django.contrib import admin
from django.urls import path
from .views import *
from paciente.views import datos_paciente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', interfaz_psicologo, name = 'interfaz'),
    path('diario_psicologo/', diario_psicologo, name='diario_psicologo'), # type: ignore
    path('datos_paciente/', datos_paciente, name='datos_paciente'),
    path('datos_psicologo/', datos_psicologo, name='datos_psicologo'),
    path('guardar_personales/', guardar_personales, name='guardar_personales'),
    path('actualizar_psicologo/', actualizar_psicologo, name='actualizar_psicologo'),
    path('guardar_cita/', guardar_cita, name='guardar_cita'),
    path('obtener_citas/', obtener_citas, name='obtener_citas'),
    path('eliminar_cita/', eliminar_cita, name='eliminar_cita'),
    path('paciente_pdf/<int:paciente_id>', paciente_pdf, name='paciente_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)