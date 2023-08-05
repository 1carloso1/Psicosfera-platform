from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name = 'login'),
    path('reestablecer_contraseña', ResContraView.as_view(), name = "reestablecer_contra"),
    path('registro', RegistroView.as_view(), name = "registro"),
]