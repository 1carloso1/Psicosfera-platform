from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

class NuevoPaciente(CreateView):
    # permission_required = '' # Dar los permisos requeridos
    model = Paciente
    form_class = FormPaciente
    # fields = '__all__'
    #success_url = reverse_lazy('usuario-registrado') #Esta vista redirije a la view que agrega el usuario al grupo Usuarios-Registrados, la cual redirijira al home
    extra_context = {'accion': 'Nuevo'}
    
      
 