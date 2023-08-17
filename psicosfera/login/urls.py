from django.urls import path
from .views import VRegistro,RegistroUsuarioView,cerrarSesion, loguear,reestablecer_contraseña, agregar_paciente, agregar_psicologo

urlpatterns = [
    path('', loguear, name = 'login'),
    path('logout', cerrarSesion, name = "logout"),
    path('reestablecer-contraseña', reestablecer_contraseña, name = "reestablecer_contra"),
    path('registro', VRegistro.as_view(), name = "registro"),
    path('registro-usuario', RegistroUsuarioView.as_view(), name = "registro-usuario"),
    # URL para agregar usuario a grupo "Pacientes"
    path('agregar-paciente/', agregar_paciente, name='agregar-paciente'),
    # URL para agregar usuario a grupo "Psicólogos"
    path('agregar-psicologo/', agregar_psicologo, name='agregar-psicologo'),
]
