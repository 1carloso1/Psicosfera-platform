from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from psicologo.especialidades import ESPECIALIDADES_CHOICES_2
from .models import Consultorio, Psicologo, User
from evento.models import Evento

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from paciente.models import Paciente, Expediente
from .forms import FormPsicologo
from django.http import  JsonResponse
import base64
from django.http import HttpResponse
from paciente.views import datos_paciente

def interfaz_psicologo(request):
    return render(request, 'interfaz-psicologo.html')

def guardar_cita(request):
    if request.method == 'POST':
        psicologo = Psicologo.objects.get(user=request.user)
        pacientes = Paciente.objects.all()
        
        for paciente in pacientes:
            if paciente.user.username == request.POST.get('paciente'):
                titulo = request.POST.get('titulo')
                fecha_inicio = request.POST.get('start').replace('-06:00',"")
                fecha_fin = request.POST.get('end').replace('-06:00',"")
                cita = Evento(paciente=paciente,psicologo=psicologo,titulo=titulo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
                cita.save()
                return JsonResponse({'mensaje': 'Cita guardado con éxito'})
        return JsonResponse({'mensaje': 'Nombre de usuario del paciente invalido'})
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
 

def datos_psicologo(request):
    psicologo = Psicologo.objects.get(user=request.user)
    psicologo_id = psicologo.id
    usuario = "registrado"
    especialidad = psicologo.especialidad
    
    if psicologo.foto_perfil:
        with psicologo.foto_perfil.open('rb') as image_file:
            image_data = image_file.read()
            foto = base64.b64encode(image_data).decode('utf-8')
    else:
        foto = None

    try:
        consultorio = Consultorio.objects.get(psicologo=psicologo_id)
        datos = {
        'usuario':usuario,
        'cons_registrado': 1,
        'foto': foto,
        'nombre': psicologo.user.first_name + ' ' + psicologo.user.last_name,
        'correo': psicologo.user.email,
        'telefono': psicologo.telefono,
        'descripcion': psicologo.descripcion,
        'especialidad' : codigoANombre(especialidad),
        'edad': psicologo.edad,
        'sexo': psicologo.sexo,
        'user': psicologo.user.username,
        "psicologo": 1,
        'facebook': psicologo.enlace_facebook,
        'linkedin': psicologo.enlace_linkedin,
        'instagram': psicologo.enlace_instagram,
        'twitter':psicologo.enlace_pagina_web,   
        'direccion' : consultorio.direccion,
        'apertura' : consultorio.horario_apertura,
        'cierre' : consultorio.horario_cierre,
    }
    except:
        datos = {
        'usuario':usuario,
        'cons_registrado': 0,
        'foto': foto,
        'nombre': psicologo.user.first_name + ' ' + psicologo.user.last_name,
        'correo': psicologo.user.email,
        'telefono': psicologo.telefono,
        'descripcion': psicologo.descripcion,
        'especialidad' : codigoANombre(especialidad),
        'edad': psicologo.edad,
        'sexo': psicologo.sexo,
        'user': psicologo.user.username,
        "psicologo": 1,
        'facebook': psicologo.enlace_facebook,
        'linkedin': psicologo.enlace_linkedin,
        'instagram': psicologo.enlace_instagram,
        'twitter':psicologo.enlace_pagina_web,   
    }
    
    return JsonResponse(datos, safe=False)
   

def codigoANombre(especialidad):
    for codigo, nombre in ESPECIALIDADES_CHOICES_2: #transforma el id en el nombre de la especialidad
    	if especialidad == codigo:
            return nombre

    
def actualizar_psicologo(request):

    if request.method == 'POST':
        psicologo = Psicologo.objects.get(user=request.user)
        psicologo.user.first_name = request.POST.get('nombre', None)
        psicologo.telefono = request.POST.get('numero', None)
        psicologo.user.email = request.POST.get('correo', None)
        psicologo.enlace_facebook = request.POST.get('facebook', None)
        psicologo.enlace_linkedin = request.POST.get('linkedin', None)
        psicologo.enlace_instagram = request.POST.get('instagram', None)
        psicologo.enlace_pagina_web = request.POST.get('twitter', None)
        psicologo.save()
        return JsonResponse({'mensaje': 'Datos guardados con exito'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
        

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
        
        return JsonResponse({'mensaje': 'Expediente guardado con éxito'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
    

def paciente_pdf(request,paciente_id):

    if paciente_id:
        paciente = Paciente.objects.get(id=paciente_id)
        nombre = str(paciente.user.last_name) + " " + str(paciente.user.first_name)
        correo_electronico = paciente.user.email
        telefono = paciente.telefono
        direccion = paciente.direccion
        edad = paciente.edad
        sexo = paciente.sexo
        foto = None

        if paciente.foto_perfil:
            with paciente.foto_perfil.open('rb') as image_file:
                image_data = image_file.read()
                foto = base64.b64encode(image_data).decode('utf-8')

        # Crear una respuesta HTTP con el contenido del PDF
        buffer = BytesIO()

        # Crear el objeto PDF
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        # Lista para contener los elementos del PDF
        elements = []

        # Estilos para el formato de texto
        styles = getSampleStyleSheet()
        titulo_style = styles["Title"]
        normal_style = styles["Normal"]

        # Añadir la imagen (foto) junto al nombre
        if foto:
            image = Image(BytesIO(base64.b64decode(foto)))
            image.drawHeight = 100
            image.drawWidth = 100

            # Crear un párrafo que contiene la imagen y el nombre
            foto_nombre_paragraph = Paragraph('<br/><br/><br/><br/><br/><br/>', normal_style)  # Añade espacio en blanco
            foto_nombre_paragraph.add(image)
            foto_nombre_paragraph.add(Spacer(1, 5))  # Espacio entre la imagen y el nombre
            foto_nombre_paragraph.add(nombre)

            elements.append(foto_nombre_paragraph)
        else:
            # Si no hay imagen, solo agrega el nombre
            elements.append(Paragraph(nombre, titulo_style))

        # Agregar otros datos con letra más pequeña
        datos = [
            "Correo Electrónico: {}".format(correo_electronico),
            "Teléfono: {}".format(telefono),
            "Dirección: {}".format(direccion),
            "Edad: {}".format(edad),
            "Sexo: {}".format(sexo),
        ]

        for dato in datos:
            elements.append(Spacer(1, 12))  # Espacio entre los datos
            elements.append(Paragraph(dato, normal_style))

        # Construir el PDF
        doc.build(elements)

        # Obtener el contenido del PDF desde el búfer y cerrar el búfer
        pdf = buffer.getvalue()
        buffer.close()

        # Configurar la respuesta HTTP
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mi_pdf.pdf"'

        # Escribir el contenido del PDF en la respuesta HTTP
        response.write(pdf)

        return response
    return JsonResponse({'mensaje': 'Selecciona a un paciente'}, status=405)