from django.shortcuts import render
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'login/login.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class RegistroView(TemplateView):
    template_name = 'registro/registro.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class RegistroUsuarioView(TemplateView):
    template_name = 'registro/registroUsuario.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class ResContraView(TemplateView):
    template_name = 'registro/reestablecer.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

