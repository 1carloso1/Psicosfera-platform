from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

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