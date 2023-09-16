from django.db import models
from django.contrib.auth.models import User
from psicologo.especialidades import ESPECIALIDADES_CHOICES_2


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

METODOS_PAGO_CHOICES = (
    ('efectivo', 'Efectivo'),
    ('tarjeta', 'Tarjeta de Crédito/Débito'),
    ('transferencia', 'Transferencia Bancaria'),
    ('paypal', 'PayPal'),
    # Agrega más métodos de pago según sea necesario
)


# Modelo de psicologo
class Psicologo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(primary_key=True, max_length=8)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField(null=True, verbose_name="Fecha de nacimiento")
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDADES_CHOICES_2)
    telefono = models.CharField(max_length=10, null=True)
    institucion_otorgamiento = models.CharField(max_length=200, blank=True, null=True, verbose_name="Institución de otorgamiento")
    anio_obtencion = models.PositiveIntegerField(null=True, verbose_name="Año de obtención")
    metodo_pago = models.CharField(max_length=100, choices=METODOS_PAGO_CHOICES, blank=True, null=True)
    curriculum = models.FileField(upload_to='curriculum_psicologo/', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='psicologos_foto_perfil/', blank=True, null=True)
    certificado = models.FileField(upload_to='certificados_psicologos/', blank=True, null=True)
    identificacion_oficial = models.FileField(upload_to='identificacion_psicologos/', blank=True, null=True) 
    enlace_pagina_web = models.URLField(blank=True, null=True)
    enlace_facebook = models.URLField(blank=True, null=True)
    enlace_instagram = models.URLField(blank=True, null=True)
    enlace_linkedin = models.URLField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

# Modelo de consultorio de los psicologos
class Consultorio(models.Model):
    psicologo = models.ForeignKey('Psicologo', verbose_name='Consultorio', on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200, blank=True)
    horario_atencion = models.CharField(max_length=200, blank=True)
    servicios_ofrecidos = models.TextField(blank=True)

    def __str__(self):
        return f"Consultorio en {self.direccion}"

    