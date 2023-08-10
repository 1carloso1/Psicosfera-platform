from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Interfaz(TemplateView):
    template_name = 'interfaz-psicologo.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

class PerfilPsicologoView(TemplateView):
    template_name = 'perfil-psicologo.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
