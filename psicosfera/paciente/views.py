from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Paciente
from .forms import FormPaciente

class PerfilView(TemplateView):
    template_name = 'perfil-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PacienteInterfazView(TemplateView):
    template_name = 'interfaz-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class NuevoPaciente(CreateView):
    # permission_required = '' # Dar los permisos requeridos
    model = Paciente
    form_class = FormPaciente
    # fields = '__all__'
    success_url = reverse_lazy('home') # Modificar la url cuando este la interfaz de usuario 
    extra_context = {'accion': 'Nuevo'}
     