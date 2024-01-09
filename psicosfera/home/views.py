from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from paciente.views import datos_paciente
from psicologo.views import codigoANombre, datos_psicologo
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from psicologo.models import Consultorio, Psicologo
from paciente.models import Paciente
from evento.models import Notification
import base64
from psicologo.forms import FormPsicologo, FormConsultorio
from paciente.forms import FormPaciente
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from psicosfera.settings import MEDIA_ROOT
        
class Home(TemplateView):
    def get_template_names(self):
        if self.request.user.groups.filter(name='Psicologos').exists(): # type: ignore
            return ['homePsicologo.html']
        else:
            return ['home.html']
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def contacto(request):
    return render(request, 'contacto.html')

@login_required
def actualizar_password(request):
    if request.method == 'POST':
        password_actual = request.POST['password_actual'] 
        nueva_password = request.POST['nueva_password']
        confirmar_password = request.POST['confirmar_password']
        # Verificar la password actual del usuario
        user = authenticate(request, username=request.user.username, password=password_actual)
        if user is not None:
            # La password actual es válida
            if nueva_password == confirmar_password:
                # Las passwords coinciden, proceder con el cambio de password
                request.user.set_password(nueva_password)
                request.user.save()
                perfil_url = reverse('perfil')
                message = "Contraseña actualizada exitosamente."
                crear_notificacion(user, message,perfil_url)
                messages.success(request, message)
                return redirect('login')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
                return redirect('perfil')
        else:
            messages.error(request, 'La contraseña actual es incorrecta.')
            return redirect('perfil')
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405) 

def enviar_correo(asunto,correo, mensaje):
    email_origen = 'chalaca23ff@gmail.com'
    recipient_list = [correo]

    email = EmailMessage(asunto, mensaje, email_origen, recipient_list)
    email.send()
    
def enviar_correo_confirmacion(request):
    # Generar token de confirmación
    usuario = request.user
    token = default_token_generator.make_token(usuario)
    print(token)
    # Construir la URL de confirmación
    url_confirmacion = reverse('confirmar_email', args=[usuario.pk, token])
    enlace_confirmacion = f'http://{settings.SITE_DOMAIN}{url_confirmacion}'
    mensaje = f'Haz clic en el siguiente enlace para confirmar tu correo: {enlace_confirmacion}'
    asunto = 'Confirma tu correo'
    
    enviar_correo(asunto,usuario.email,mensaje)
    return redirect('perfil')


def confirmar_correo(request, pk, token):
    print(token)
    usuario = get_object_or_404(User, pk=pk)
    try:
        usuario_paciente = Paciente.objects.get(user=usuario)
        
        if default_token_generator.check_token(usuario_paciente.user, token):
            usuario_paciente.correo_verificado = True
            usuario_paciente.save()
            return HttpResponse('Correo electrónico confirmado exitosamente para el Paciente.')
        else:
            return HttpResponse('Enlace de confirmación no válido.')
    except Paciente.DoesNotExist:
       print("Usuario Paciente no encontrado")
       
    try:
        usuario_psicologo = Psicologo.objects.get(user=usuario)
        
        if default_token_generator.check_token(usuario_psicologo.user, token):
            usuario_psicologo.correo_verificado = True
            usuario_psicologo.save()
            return HttpResponse('Correo electrónico confirmado exitosamente para el Psicologo.')
        else:
            return HttpResponse('Enlace de confirmación no válido.')
    except Psicologo.DoesNotExist:
        print("Usuario Psicologo no encontrado")
    
    return HttpResponse('Enlace de confirmación no válido para ningun usuario.')

    
     
def crear_notificacion(user, mensaje, url):
    Notification.objects.create(user=user, mensaje=mensaje, notification_url=url)
    asunto = 'Cambios en tu cuenta'
    enviar_correo(asunto,user.email, mensaje)
    
def marcar_notificacion_leida(request):
    if request.method == 'POST':
        notification_url = request.POST.get('notification_url', '')
        notification_id = request.POST.get('notification_id', '')
        if notification_id:
            try:
                # Obtén la notificación basada en la URL
                notification = Notification.objects.get(id=notification_id, user=request.user)
                notification.is_read = True
                notification.save()
                return JsonResponse({'success': True, 'redirect_url': notification_url})
            except Notification.DoesNotExist:
                pass

    return JsonResponse({'success': False})

def perfil(request):

    if request.user.groups.filter(name='Psicologos').exists():
        psicologo=Psicologo.objects.get(user=request.user)
        consultorio = Consultorio.objects.get(psicologo=psicologo)
        datos = {
            'direccion' : consultorio.direccion,
            
        }   
        formConsultorio = FormConsultorio(instance=consultorio)
        formPsicologo = FormPsicologo(instance=psicologo)
        return render(request, 'perfil_psicologo_privado.html', {'formPsicologo': formPsicologo, 'formConsultorio': formConsultorio,'usuario': datos, 'correo_verificado' : psicologo.correo_verificado})
    elif request.user.groups.filter(name='Pacientes').exists():
        paciente=Paciente.objects.get(user=request.user)
        form = FormPaciente(instance=paciente)
        return render(request, 'perfil_paciente.html', {'form': form, 'correo_verificado' : paciente.correo_verificado})
    else:
        return redirect('login')
    
def exito_actualizacion(request):
    return HttpResponseRedirect(reverse('perfil') + '?success=true')

def agregar_contacto(request, username):
    #La idea general es que obtenga al usuario actual (debe ser paciente) y al psicologo que es el username de la URL
    user = get_object_or_404(User, username=username)
    paciente = get_object_or_404(Paciente, user=request.user)
    try:
        psicologo = Psicologo.objects.get(user=user)
     
        if not paciente.contactos:
            paciente.contactos = []
        if psicologo.id not in paciente.contactos:
            paciente.contactos.append(psicologo.id)
        paciente.save()

        if not psicologo.contactos:
            psicologo.contactos = []
        if paciente.id not in psicologo.contactos:
            psicologo.contactos.append(paciente.id)
        psicologo.save()

        print("paciente: ")
        print(paciente.contactos)
        print("psicologo: ")
        print(psicologo.contactos)

        # Respuesta JSON para confirmar el éxito
        return JsonResponse({"message": "Contacto agregado exitosamente"})

    except Psicologo.DoesNotExist:
        # Si el psicólogo no existe, devolvemos un mensaje de error
        return JsonResponse({"error": "El psicólogo no existe"})
    except Paciente.DoesNotExist:
        # Si el paciente no existe, devolvemos un mensaje de error
        return JsonResponse({"error": "El paciente no existe"})
 
def perfilPublico(request, username):
    # Obtener el usuario basado en el username
    user = get_object_or_404(User, username=username)
    paciente = get_object_or_404(Paciente, user=request.user)
    
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

        #Verificar que los usuarios (Paciente y Psicologo tienen una relacion)
        if not psicologo.contactos:
            usuario_agregado = 0
        elif paciente.id in psicologo.contactos:
            usuario_agregado = 1
        else:
            usuario_agregado = 0
        print(usuario_agregado)
        datos = {
        'nombre': psicologo.user.first_name,
        'apellidos' : psicologo.user.last_name,
        'foto': foto,
        'correo': psicologo.user.email,
        'telefono': psicologo.telefono,
        'institucion': psicologo.institucion_otorgamiento,
        'ubicacion': psicologo.ubicacion,
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
        'costo_consulta':consultorio.costo_consulta, 
        'usuario_agregado': usuario_agregado, 
    }
        return render(request, 'perfil_psicologo.html', {'usuario': datos})
    
    except Psicologo.DoesNotExist:
        try:
            paciente = Paciente.objects.get(user=user)
            if paciente.foto_perfil:
                with paciente.foto_perfil.open('rb') as image_file:
                    image_data = image_file.read()
                    foto = base64.b64encode(image_data).decode('utf-8')
            else:
                foto = None

            datos = {
            'nombre': paciente.user.first_name,
            'apellidos' : paciente.user.last_name,
            'foto': foto,
            'correo': paciente.user.email,
            'telefono': paciente.telefono,
            'ubicacion': paciente.ubicacion,
            'edad': paciente.edad,
            'sexo': paciente.sexo,
            'user': paciente.user.username,
            "psicologo": 0,
            'descripcion' : paciente.descripcion,
            'usuario_agregado': 0,
            #'facebook': psicologo.enlace_facebook,
            #'linkedin': psicologo.enlace_linkedin,
            #'instagram': psicologo.enlace_instagram,
            #'twitter':psicologo.enlace_pagina_web,    
            }
            return render(request, 'perfil_paciente_publico.html', {'usuario': datos})
        except Paciente.DoesNotExist:
            pass

@login_required
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
