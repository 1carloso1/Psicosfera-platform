from django.urls import path
from .views import procesar_formulario, Home, contacto

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_datos/', procesar_formulario, name='contacto_datos'),
]