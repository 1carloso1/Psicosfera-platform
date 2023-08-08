from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PerfilView.as_view(), name = 'perfil'),
]