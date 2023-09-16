from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
import googlemaps
from django.conf import settings
from psicologo.models import Psicologo
from psicologo.especialidades import ESPECIALIDADES_CHOICES,ESPECIALIDADES_CHOICES_2
from django.db.models import F, Value, CharField

class PerfilView(TemplateView):
    template_name = 'perfil-paciente.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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
                for codigo, nombre in ESPECIALIDADES_CHOICES_2: #transforma el id en en nombre de la especialidad
                    if especialidad == codigo:
                        especialidad = nombre
                        break  # Terminamos el bucle cuando encontramos una coincidencia
                if especialidad == inputText: #verifica si la especialidad del usuario es la que se esta solicitando
                    nombre_usuario = psicologo.user.first_name + " "  +  psicologo.user.last_name # Accede al nombre de usuario del usuario asociado al psicólogo
                    lista_nombres.append(nombre_usuario)  # Agrega el nombre de usuario a la lista
            return JsonResponse(lista_nombres, safe=False)
        
        elif inputText not in ESPECIALIDADES_CHOICES:
            # Realiza una consulta para obtener todos los objetos Psicologos
            psicologos = Psicologo.objects.all()
            for psicologo in psicologos:
                nombre = psicologo.user.first_name + " "  +  psicologo.user.last_name # Accede al nombre de usuario del usuario asociado al psicólogo
                especialidad = psicologo.especialidad # Accede a la especialidad del psicologo
                for codigo, esp in ESPECIALIDADES_CHOICES_2: #transforma el id en en nombre de la especialidad
                    if especialidad == codigo:
                        especialidad = esp
                        break  # Terminamos el bucle cuando encontramos una coincidencia
                if nombre ==  inputText:
                    lista_nombres.append((nombre,especialidad))  # Agrega el nombre de usuario a la lista
            return JsonResponse(lista_nombres, safe=False)
        
        else:
            #Si no cumple nada de esto regresa una lista vacia
            return JsonResponse(lista_nombres, safe=False)
        # Devolver las sugerencias como un objeto JSON
    


   




    
      
 