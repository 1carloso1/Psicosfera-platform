from django.db import models
from paciente.models import Paciente
from psicologo.models import Psicologo
from django.utils import timezone
# Modelo para las citas
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, verbose_name="Psicologo", on_delete=models.CASCADE)
    fecha_cita = models.DateField(verbose_name="Fecha de cita")
    
    def __str__(self):
        return str(self.paciente) +"|"+" Prox. cita: "+ str(self.fecha_cita)