from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from psicosfera.utils import UsuarioRegistradoRequiredMixin
from .models import Paciente
from .forms import FormPaciente
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
import base64

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



class DatosPerfilView(View):
    def get(self, request):
        paciente_id = request.GET.get('paciente_id')
        try:
            paciente = Paciente.objects.get(id=paciente_id)
            nombre = str(paciente.nombre) + " " + str(paciente.apaterno) + " " + str(paciente.amaterno)
            correo_electronico = paciente.correo
            telefono = paciente.telefono
            direccion = paciente.direccion
            edad = paciente.edad
            sexo = paciente.sexo
            ocupacion = paciente.ocupacion
            fecha_nacimiento = paciente.fecha_nacimiento
            if paciente.foto_perfil:
                with paciente.foto_perfil.open('rb') as image_file:
                    image_data = image_file.read()
                    foto = base64.b64encode(image_data).decode('utf-8')
            else:
                foto = None

            contexto = {
                'nombre': nombre,
                'fecha_nacimiento': fecha_nacimiento,
                'edad': edad,
                'sexo': sexo,
                'ocupacion': ocupacion,
                'correo_electronico': correo_electronico,
                'telefono': telefono,
                'direccion': direccion,
                'foto': foto,
            }

            return render(request, 'perfil-paciente.html', contexto)
        except Paciente.DoesNotExist:
            return HttpResponse("Paciente no encontrado.", status=404)