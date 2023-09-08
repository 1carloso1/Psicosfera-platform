from django.db import models
from django.contrib.auth.models import User
from psicologo.models import Psicologo



SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Modelo de paciente
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    ocupacion = models.CharField(max_length=100, verbose_name="Ocupación")
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200, blank=True, verbose_name="Dirección")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='pacientes_foto_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

# Modelo de expediente de un paciente
class Expediente(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    notas_personales = models.TextField(blank=True)
    notas_compartidas = models.TextField(blank=True)


    def __str__(self):
        return f"Expediente #{self.id} - Paciente: {self.paciente.user.last_name} {self.paciente.user.first_name}"

    