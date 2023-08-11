from django.urls import path
from .views import VRegistro,RegistroUsuarioView,cerrarSesion, loguear,reestablecer_contraseña

urlpatterns = [
    path('', loguear, name = 'login'),
    path('logout', cerrarSesion, name = "logout"),
    path('reestablecer-contraseña', reestablecer_contraseña, name = "reestablecer_contra"),
    path('registro', VRegistro.as_view(), name = "registro"),
    path('registro-usuario', RegistroUsuarioView.as_view(), name = "registro-usuario"),
]