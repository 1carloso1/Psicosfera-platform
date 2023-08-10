from django.shortcuts import render
from django.views.generic import TemplateView

class PerfilView(TemplateView):
    template_name = 'perfil-usuario.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PacienteInterfazView(TemplateView):
    template_name = 'interfaz-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
