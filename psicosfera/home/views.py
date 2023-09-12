from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail

class Home(TemplateView):
    def get_template_names(self):
        if self.request.user.groups.filter(name='Psicologos').exists():
            return ['homePsicologo.html']
        else:
            return ['home.html']
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']

        # Enviar el correo electrónico
        send_mail(
            'Nuevo mensaje desde el formulario de contacto',
            f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
            'tucorreo@gmail.com',  # Dirección de correo del remitente (debe ser la misma que configuraste antes)
            ['destinatario@example.com'],  # Dirección de correo del destinatario
            fail_silently=False,
        )

        # Redirigir a una página de éxito
        return redirect('exito')  

    return render(request, 'formulario.html')  # Renderiza el formulario si el método no es POST    
    
