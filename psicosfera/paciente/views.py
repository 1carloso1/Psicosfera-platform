from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
import googlemaps
from django.conf import settings
from psicologo.models import Psicologo

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

    # Supongamos que tienes una lista de sugerencias de especialidades
    sugerencias = [
        'Psicología Clínica',
        'Psicología Educativa',
        'Psicología del Deporte',
        'Psicología Organizacional',
        'Psicología Forense',
        'Salud Mental',
        'Terapia Familiar',
        'Neuropsicología',
        'Psicología Infantil',
        'Psicoterapia',
        'Psicología Social',
        'Gerontología',
        'Psicología de la Rehabilitación',
        'Psicología Educacional',
        'Psicología Legal',
        'Orientación Vocacional',
        'Terapia Sexual',
        'Terapia de Pareja',
        'Psicología Transpersonal'
    ]

    
    # Realiza una consulta para obtener todos los objetos Psicologos
    psicologos = Psicologo.objects.all()

    # Crea una lista de nombres completos a partir de los objetos Psicologo
    nombres_completos_de_psicologos = []

    for psicologo in psicologos:
        # Combina el primer nombre y el apellido
        nombre_completo = nombre_completo = f"{psicologo.user.first_name} {psicologo.user.last_name}"
        nombres_completos_de_psicologos.append(nombre_completo)


    sugerencias_total = sugerencias + nombres_completos_de_psicologos

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






    
      
 