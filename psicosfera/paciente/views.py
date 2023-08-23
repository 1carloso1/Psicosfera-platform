from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from psicosfera.utils import UsuarioRegistradoRequiredMixin
from .models import Paciente
from .forms import FormPaciente
from django.contrib.auth.models import Group
from django.shortcuts import redirect

class PerfilView(TemplateView):
    template_name = 'perfil-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PacienteInterfazView(TemplateView):
    template_name = 'interfaz-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class NuevoPaciente(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = FormPaciente
    extra_context = {'accion': 'Nuevo'}

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Usuario-Registrado').exists():
            return redirect('home')  # Ajusta 'home' a la URL correcta
        else:
            return super().dispatch(request, *args, **kwargs)


    
      
 