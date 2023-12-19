import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from paciente.views import datos_paciente, actualizar_paciente
from psicologo.views import codigoANombre, datos_psicologo, actualizar_psicologo
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from psicologo.models import Consultorio, Psicologo
from paciente.models import Paciente
from django.templatetags.static import static
import base64

from psicosfera.settings import MEDIA_ROOT

def guardar_datos(request):
    if request.method == 'POST':
        esPsicologo = request.POST.get("psicologo")
        if esPsicologo == "1":
            return actualizar_psicologo(request)
        else:
            return actualizar_paciente(request)


class Home(TemplateView):
    def get_template_names(self):
        if self.request.user.groups.filter(name='Psicologos').exists():
            return ['homePsicologo.html']
        else:
            return ['home.html']
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def contacto(request):
    return render(request, 'contacto.html')
    
def perfil(request):
    datos = {}

    if request.user.groups.filter(name='Psicologos').exists():
        return render(request, 'perfil_psicologo_privado.html')
    else:
        response = datos_paciente(request)
        datos = json.loads(response.content)
        return render(request, 'perfil_paciente.html', datos)

 
def perfilPublico(request, username):
    # Obtener el usuario basado en el username
    user = get_object_or_404(User, username=username)
    
    # Intentar obtener el perfil de psicólogo para el usuario
    try:
        psicologo = Psicologo.objects.get(user=user)
        consultorio = Consultorio.objects.get(psicologo=psicologo)
        especialidad = psicologo.especialidad
        if psicologo.foto_perfil:
            with psicologo.foto_perfil.open('rb') as image_file:
                image_data = image_file.read()
                foto = base64.b64encode(image_data).decode('utf-8')
        else:
            foto = None
        if psicologo.certificado:
            with psicologo.certificado.open('rb') as pdf_file:
                pdf_data = pdf_file.read()
                certificado = base64.b64encode(pdf_data).decode('utf-8')
        else:
            certificado = None
        if psicologo.curriculum:
            with psicologo.curriculum.open('rb') as pdf_file:
                pdf_data = pdf_file.read()
                curriculum = base64.b64encode(pdf_data).decode('utf-8')
        else:
            curriculum = None

        datos = {
        'nombre': psicologo.user.first_name + ' ' + psicologo.user.last_name,
        'foto': foto,
        'correo': psicologo.user.email,
        'telefono': psicologo.telefono,
        'institucion': psicologo.institucion_otorgamiento,
        'especialidad' : codigoANombre(especialidad),
        'institucion': psicologo.institucion_otorgamiento,
        'cedula': psicologo.cedula,
        'descripcion' : psicologo.descripcion,
        'direccion' : consultorio.direccion,
        'apertura' : consultorio.horario_apertura,
        'cierre' : consultorio.horario_cierre,
        'edad': psicologo.edad,
        'sexo': psicologo.sexo,
        'user': psicologo.user.username,
        "psicologo": 1,
        'facebook': psicologo.enlace_facebook,
        'linkedin': psicologo.enlace_linkedin,
        'instagram': psicologo.enlace_instagram,
        'twitter':psicologo.enlace_pagina_web,   
        'certificado':certificado,   
        'curriculum':curriculum, 
    }
        print(foto)
        return render(request, 'perfil_psicologo.html', {'usuario': datos})
    except Psicologo.DoesNotExist:
        pass  # El usuario no es un psicólogo, continuar
    
    # Intentar obtener el perfil de paciente para el usuario
    try:
        perfil_paciente = Paciente.objects.get(user=user)
        return render(request, 'perfil_paciente.html', {'usuario': perfil_paciente})
    except Paciente.DoesNotExist:
        pass  # El usuario no es un paciente, continuar
    
    # Si no es psicólogo ni paciente, puedes manejarlo de acuerdo a tus necesidades
    return render(request, 'perfil_no_encontrado.html', {'usuario': username}) 

def datos(request):
    if request.user.groups.filter(name='Psicologos').exists():
        return datos_psicologo(request)
    elif request.user.groups.filter(name='Pacientes').exists():
        return datos_paciente(request)
    else:
        return datos_default(request)
    
def datos_default(request):
    usuario = "default"
    data ={
        'usuario':usuario,
    }
    return JsonResponse(data, safe=False)



def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST['firstName']
        apellido = request.POST['lastName']
        correo = request.POST['email']
        telefono = request.POST['phone']
        mensaje = request.POST['message']
        asunto = "Contacto de la pagina web."
        
        template = render_to_string('email.html', {
            'nombre': nombre,
            'apellido':apellido,
            'correo': correo,
            'telefono': telefono,
            'mensaje': mensaje,
        })

        email = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['chalaca23ff@gmail.com']
        )

        email.fail_silently = False 
        email.send()

        messages.success(request, "Se ha enviado tu correo.")
        return redirect('contacto')