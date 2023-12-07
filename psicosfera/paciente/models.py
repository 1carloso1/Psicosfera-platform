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
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=False, blank=False)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    ocupacion = models.CharField(max_length=100, verbose_name="Ocupación", null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    direccion = models.CharField(max_length=200, verbose_name="Dirección", null=False, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='pacientes_foto_perfil/', blank=True) 
    descripcion = models.CharField(max_length=254, blank=True, null=True, verbose_name="Descripción")

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

    