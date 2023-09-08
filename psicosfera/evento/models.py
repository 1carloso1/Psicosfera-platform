from django.db import models
from paciente.models import Paciente
from psicologo.models import Psicologo

# Create your models here.
class Evento(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, verbose_name="Psicologo", on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    titulo = models.CharField(max_length=255)
    