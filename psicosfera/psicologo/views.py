from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Psicologo
from .forms import FormPsicologo

# Create your views here.
class Interfaz(TemplateView):
    template_name = 'interfaz-psicologo.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PerfilPsicologoView(TemplateView):
    template_name = 'perfil-psicologo.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class NuevoPsicologo(CreateView):
    # permission_required = '' # Dar los permisos requeridos
    model = Psicologo
    form_class = FormPsicologo
    # fields = '__all__'
    success_url = reverse_lazy('home') # Modificar la url cuando este la interfaz de usuario 
    extra_context = {'accion': 'Nuevo'}
