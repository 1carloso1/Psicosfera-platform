from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Psicologo, User
from evento.models import Evento

from paciente.models import Paciente, Expediente
from .forms import FormPsicologo
from django.http import HttpResponse, JsonResponse
import base64

def interfaz_psicologo(request):
    return render(request, 'interfaz-psicologo.html')

def guardar_cita(request):
    if request.method == 'POST':
        psicologo = Psicologo.objects.get(user=request.user)
        pacientes = Paciente.objects.all()
        for paciente in pacientes:
            if paciente.user == request.POST.get('paciente'):
                break
        titulo = request.POST.get('titulo')
        fecha_inicio = request.POST.get('start').replace('-06:00',"")
        fecha_fin = request.POST.get('end').replace('-06:00',"")
        cita = Evento(paciente=paciente,psicologo=psicologo,titulo=titulo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
        cita.save()

        return JsonResponse({'mensaje': 'Cita guardado con éxito'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def eliminar_cita(request):
    try:
        cita = Evento.objects.get(id=request.POST.get('id'))
        cita.delete()
        return JsonResponse({'mensaje': 'Cita eliminada con éxito'})
    except Evento.DoesNotExist:
        return JsonResponse({'mensaje': 'La cita no existe'}, status=404)

def obtener_citas(request):
    psicologo = Psicologo.objects.get(user=request.user)
    
    citas = Evento.objects.all()
    citasPsicologo = []
    for cita in citas:
        if cita.psicologo == psicologo:
            citasPsicologo.append({
                'id': cita.id,
                'id_paciente': cita.paciente.id,
                'nombre_paciente': cita.paciente.user.first_name + ' ' + cita.paciente.user.last_name,
                'title': cita.titulo,
                'start': cita.fecha_inicio.strftime('%Y-%m-%dT%H:%M:%S'),  # Formato ISO8601  
                'end': cita.fecha_fin.strftime('%Y-%m-%dT%H:%M:%S'), # Formato ISO8601 
                'fecha_inicio': cita.fecha_inicio.strftime('%Y-%m-%d'),   
                'fecha_fin': cita.fecha_fin.strftime('%Y-%m-%d'),# Formato ISO8601
                'hora_fin': cita.fecha_fin.strftime('%H:%M:%S'),  # Formato ISO8601
                'hora_inicio': cita.fecha_inicio.strftime('%H:%M:%S'),  # Formato ISO8601
            })
    return JsonResponse(citasPsicologo, safe=False)


def perfil_psicologo(request):

    psicologo = Psicologo.objects.get(user=request.user)
    if psicologo.foto_perfil:
        with psicologo.foto_perfil.open('rb') as image_file:
            image_data = image_file.read()
            foto = base64.b64encode(image_data).decode('utf-8')
    else:
        foto = None
    datos = {
        'nombre': psicologo.user.first_name + ' ' + psicologo.user.last_name,
        'edad': psicologo.edad,
        'foto': foto,
        'correo': psicologo.user.email,
        'numero': psicologo.telefono,
    }
    return render(request, 'perfil-psicologo.html', context=datos)
    
    

def datos_paciente(request):
    if request.method == 'POST':   
        
        paciente_id = request.POST.get('paciente_id')
        paciente = Paciente.objects.get(id=paciente_id)
        nombre = str(paciente.user.last_name) +" "+str(paciente.user.first_name)
        correo_electronico = paciente.user.email
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
            notas_compartidas = expediente.notas_compartidas
            notas_personales = expediente.notas_personales
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
                "notas_compartidas" : notas_compartidas,
                "notas_personales": notas_personales,
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

def guardar_notas(request):
    if request.method == 'POST':
        notas_compartidas = request.POST.get('contenidoCompartidas', None)
        if(not notas_compartidas):
            notas_compartidas = ""
        notas_personales = request.POST.get('contenidoPersonales', None)
        if(not notas_personales):
            notas_personales = ""
        paciente_id = request.POST.get('id', None)
        
        paciente = Paciente.objects.get(id=paciente_id)
        try:
            expediente = Expediente.objects.get(paciente=paciente)
            expediente.notas_personales = notas_personales
            expediente.notas_compartidas = notas_compartidas
            expediente.save()
        except:
            psicologo = Psicologo.objects.get(user=request.user)
            expediente = Expediente(paciente=paciente,psicologo = psicologo,notas_compartidas = notas_compartidas,notas_personales = notas_personales)
            expediente.save()
        return JsonResponse({'notas_personales': expediente.notas_personales, 'notas_compartidas': expediente.notas_compartidas})
    
    HttpResponse("Metodo no valido.",status=405)
    