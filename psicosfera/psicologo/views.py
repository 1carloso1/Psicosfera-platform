from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Psicologo
from paciente.models import Paciente, Expediente
from .forms import FormPsicologo
from django.http import JsonResponse

# Create your views here.
class Interfaz(ListView):
    model = Paciente  # Establece el modelo al que quieres acceder
    template_name = 'interfaz-psicologo.html'
    context_object_name = 'pacientes'  # Define el nombre de la variable

    
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
    
def datos_paciente(request, pk):
    pacientes = Paciente.objects.all()
    paciente = Paciente.objects.get(id=pk)
    try:
        expediente = Expediente.objects.get(paciente=paciente)
        return render(request, 'interfaz-psicologo.html', {'paciente_seleccionado': paciente, 'pacientes': pacientes, 'expediente': expediente})
    except:
        print("Expediente no encontrado")
        return render(request, 'interfaz-psicologo.html', {'paciente_seleccionado': paciente, 'pacientes': pacientes})
        
def guardar_notas_personales(request,pk):
    if request.method == 'POST':
        notas_personales = request.POST.get('diagnostico', None)
        print(request)
        
        paciente = Paciente.objects.get(id=pk)
        expediente = Expediente.objects.get(paciente=paciente)
        expediente.observaciones = notas_personales
    return redirect('interfaz')


def guardar_notas_compartidas(request,pk):
    if request.method == 'POST':
        notas_compartidas = request.POST.get('notas_compartidas', None)
        print(notas_compartidas)
        paciente = Paciente.objects.get(id=pk)
        expediente = Expediente.objects.get(paciente=paciente)
        expediente.diagnostico = notas_compartidas
        
    return redirect('interfaz')