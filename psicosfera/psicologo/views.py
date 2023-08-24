from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Psicologo
from paciente.models import Paciente, Expediente
from .forms import FormPsicologo
from django.http import HttpResponse, JsonResponse
import base64

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
    
def datos_paciente(request):
    if request.method == 'POST':   
        print(request)     
        paciente_id = request.POST.get('paciente_id')
        paciente = Paciente.objects.get(id=paciente_id)
        nombre = str(paciente.nombre) +" "+str(paciente.apaterno) +" "+ str(paciente.amaterno)
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
            
        try:
            expediente = Expediente.objects.get(paciente=paciente)
            diagnostico = expediente.diagnostico
            tratamiento = expediente.tratamiento
            return JsonResponse({
                "foto": foto,
                "nombre" : nombre,
                "correo_electronico" : correo_electronico,
                "telefono" : telefono,
                "direccion" : direccion,
                "edad" : edad,
                "sexo" : sexo,
                "ocupacion" : ocupacion,
                "fecha_nacimiento" : fecha_nacimiento,
                "diagnostico" : diagnostico,
                "tratamiento": tratamiento,
            })
        except:
            print("No hay expediente.")
            return JsonResponse({
                "foto": foto,
                "nombre" : nombre,
                "correo_electronico" : correo_electronico,
                "telefono" : telefono,
                "direccion" : direccion,
                "edad" : edad,
                "sexo" : sexo,
                "ocupacion" : ocupacion,
                "fecha_nacimiento" : fecha_nacimiento,
            })
    HttpResponse("Metodo no valido.",status=405)
    
    
def guardar_notas_personales(request):
    if request.method == 'POST':
        notas_personales = request.POST.get('textareaContent', None)
        print(request)
        
        paciente = Paciente.objects.get(id=pk)
        expediente = Expediente.objects.get(paciente=paciente)
        expediente.observaciones = notas_personales
    HttpResponse("Metodo no valido.",status=405)
    


def guardar_compartidas(request):
    if request.method == 'POST':
        print(request)
        notas_compartidas = request.POST.get('textareaContent', None)
        paciente_id = request.POST.get('id', None)
        
        paciente = Paciente.objects.get(id=paciente_id)
        expediente = Expediente.objects.get(paciente=paciente)
        expediente.diagnostico = notas_compartidas
        return JsonResponse({'diagnostico': expediente.diagnostico })
    
    HttpResponse("Metodo no valido.",status=405)
    