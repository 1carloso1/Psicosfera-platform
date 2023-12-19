from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
import googlemaps
from django.conf import settings
from psicologo.models import Psicologo, Consultorio
from psicologo.especialidades import ESPECIALIDADES_CHOICES,ESPECIALIDADES_CHOICES_2
from django.db.models import F, Value, CharField
from django.shortcuts import render
from django.http import HttpResponse
from paciente.models import Paciente, Expediente
import base64


def datos_paciente(request):
    try:
        paciente_id = request.POST.get('paciente_id')
        paciente = Paciente.objects.get(id=paciente_id)
    except:
        paciente = Paciente.objects.get(user=request.user)
    nombre = str(paciente.user.first_name) +" "+ str(paciente.user.last_name)
    correo_electronico = paciente.user.email
    descripcion = paciente.descripcion
    telefono = paciente.telefono
    direccion = paciente.direccion
    edad = paciente.edad
    sexo = paciente.sexo
    usuario = "registrado"
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
        data ={
            'usuario':usuario,
            "foto": foto,
            "nombre" : nombre,
            "correo" : correo_electronico,
            'descripcion': descripcion,
            "telefono" : telefono,
            "direccion" : direccion,
            "edad" : edad,
            "sexo" : sexo,
            "user": paciente.user.username,
            "psicologo": 0,
            
            "notas_compartidas" : notas_compartidas,
            "notas_personales": notas_personales,
        }
    except:
        print("No hay expediente.")
        data ={
            'usuario':usuario,
            "foto": foto,
            "nombre" : nombre,
            "correo" : correo_electronico,
            'descripcion': descripcion,
            "telefono" : telefono,
            "direccion" : direccion,
            "edad" : edad,
            "sexo" : sexo,
            "user": paciente.user.username,
            "psicologo": 0,
            
        }
    return JsonResponse(data, safe=False)

def actualizar_paciente(request):

    if request.method == 'POST':
        paciente = Paciente.objects.get(user=request.user)
        paciente.user.first_name = request.POST.get('nombre', None)
        paciente.telefono = request.POST.get('numero', None)
        paciente.user.email = request.POST.get('correo', None)
        paciente.save()
        return JsonResponse({'mensaje': 'Datos guardados con exito'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
        

    
class PacienteInterfazView(TemplateView):
    template_name = 'interfaz-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
def autocompletar_especialidades(request):
    query = request.GET.get('query', '')
    
    # Realiza una consulta para obtener todos los objetos Psicologos
    psicologos = Psicologo.objects.all()

    # Crea una lista de nombres completos a partir de los objetos Psicologo
    nombres_completos_de_psicologos = []

    for psicologo in psicologos:
        # Combina el primer nombre y el apellido
        nombre_completo = nombre_completo = f"{psicologo.user.first_name} {psicologo.user.last_name}"
        nombres_completos_de_psicologos.append(nombre_completo)


    sugerencias_total = ESPECIALIDADES_CHOICES + nombres_completos_de_psicologos

    # Filtrar las sugerencias que coinciden con la consulta del usuario
    sugerencias_filtradas = [s for s in sugerencias_total if query.lower() in s.lower()]

    # Devolver las sugerencias como un objeto JSON
    return JsonResponse(sugerencias_filtradas, safe=False)


def autocompletar_ubicaciones(request):
    query = request.GET.get('query', '')

    if query:
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        places = gmaps.places_autocomplete(input_text=query)

        suggestions = [place['description'] for place in places]

        return JsonResponse(suggestions, safe=False)

    return JsonResponse([], safe=False)

#Este metodo filtrara los psicologos por la especilidad ingresada o su nombre
def psicologos_por_especialidad_nombre(request):
     lista_nombres = []

     if request.method == 'GET':
        inputText = request.GET.get('especialidad')

        #Primero verificamos si esta en la lista de especialidades
        if inputText in ESPECIALIDADES_CHOICES:
            # Obtén todos los objetos Psicologo
            psicologos = Psicologo.objects.all()
            for psicologo in psicologos:
                especialidad = psicologo.especialidad # Accede a la especialidad del psicologo
                if psicologo.foto_perfil:
                    with psicologo.foto_perfil.open('rb') as image_file:   #Obtiene la foto encriptada para mostrarla en la tarjeta
                        image_data = image_file.read()
                        foto = base64.b64encode(image_data).decode('utf-8')
                else:
                    foto = None
                for codigo, nombre in ESPECIALIDADES_CHOICES_2: #transforma el id en en nombre de la especialidad
                    if especialidad == codigo:
                        especialidad = nombre
                        break  # Terminamos el bucle cuando encontramos una coincidencia
                if especialidad == inputText: #verifica si la especialidad del usuario es la que se esta solicitando
                    #Ya que sabemos que tiene la esp solicitada, buscaremos su respectivo consultorio
                    consultorio = Consultorio.objects.get(psicologo=psicologo)
                    direccion_consultorio = consultorio.direccion
                    direccion_consultorio = direccion_consultorio.replace(',', '-')
                    nombre_usuario = psicologo.user.first_name + " "  +  psicologo.user.last_name # Accede al nombre de usuario del usuario asociado al psicólogo
                    username = psicologo.user.username
                    lista_nombres.append((nombre_usuario,especialidad, direccion_consultorio, username, foto))  # Agrega el nombre de usuario a la lista
            return JsonResponse(lista_nombres, safe=False)
        
        elif inputText not in ESPECIALIDADES_CHOICES:
            # Realiza una consulta para obtener todos los objetos Psicologos
            psicologos = Psicologo.objects.all()
            for psicologo in psicologos:
                nombre = psicologo.user.first_name + " "  +  psicologo.user.last_name # Accede al nombre de usuario del usuario asociado al psicólogo
                especialidad = psicologo.especialidad # Accede a la especialidad del psicologo
                if psicologo.foto_perfil:
                    with psicologo.foto_perfil.open('rb') as image_file:   #Obtiene la foto encriptada para mostrarla en la tarjeta
                        image_data = image_file.read()
                        foto = base64.b64encode(image_data).decode('utf-8')
                else:
                    foto = None
                for codigo, esp in ESPECIALIDADES_CHOICES_2: #transforma el id en en nombre de la especialidad
                    if especialidad == codigo:
                        especialidad = esp
                        break  # Terminamos el bucle cuando encontramos una coincidencia
                if nombre ==  inputText:
                    #Ya que sabemos que tiene la esp solicitada, buscaremos su respectivo consultorio
                    consultorio = Consultorio.objects.get(psicologo=psicologo)
                    direccion_consultorio = consultorio.direccion
                    direccion_consultorio = direccion_consultorio.replace(',', '-')
                    username = psicologo.user.username
                    lista_nombres.append((nombre,especialidad,direccion_consultorio, username, foto))  # Agrega el nombre de usuario a la lista
            return JsonResponse(lista_nombres, safe=False)
        
        else:
            #Si no cumple nada de esto regresa una lista vacia
            return JsonResponse(lista_nombres, safe=False)
        # Devolver las sugerencias como un objeto JSON
    


   




    
      
 