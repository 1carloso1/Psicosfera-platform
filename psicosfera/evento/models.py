from django.db import models
from paciente.models import Paciente
from psicologo.models import Psicologo
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, verbose_name="Psicologo", on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    titulo = models.CharField(max_length=255)
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_url = models.URLField(blank=True, null=True)