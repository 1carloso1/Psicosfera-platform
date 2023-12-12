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
    if request.user.groups.filter(name='Psicologos').exists():
        return render(request, 'perfil_psicologo_privado.html')
    else:
        return render(request, 'perfil_paciente.html')


def perfilPublico(request, username):
    # Obtener el usuario basado en el username
    user = get_object_or_404(User, username=username)
    
    # Intentar obtener el perfil de psicólogo para el usuario
    try:
        psicologo = Psicologo.objects.get(user=user)
        consultorio = Consultorio.objects.get(psicologo=psicologo)
        especialidad = psicologo.especialidad
        datos = {
        'nombre': psicologo.user.first_name + ' ' + psicologo.user.last_name,
        'correo': psicologo.user.email,
        'telefono': psicologo.telefono,
        'especialidad' : codigoANombre(especialidad),
        'direccion' : consultorio.direccion,
        'horario' : consultorio.horario_atencion,
        'edad': psicologo.edad,
        'sexo': psicologo.sexo,
        'user': psicologo.user.username,
        "psicologo": 1,
        'facebook': psicologo.enlace_facebook,
        'linkedin': psicologo.enlace_linkedin,
        'instagram': psicologo.enlace_instagram,
        'twitter':psicologo.enlace_pagina_web,   
    }
    
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
    try:
        return datos_psicologo(request)
    except:
        return datos_paciente(request)
    



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