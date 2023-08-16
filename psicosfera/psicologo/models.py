from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Modelo de psicologo
class Psicologo(models.Model):
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=120, verbose_name="Primer Apellido")
    amaterno= models.CharField(max_length=120, verbose_name="Segundo Apellido")
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    especialidad = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    ubicacion = models.TextField()
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='psicologos_foto_perfil/', blank=True, null=True)
    certificado_pdf = models.FileField(upload_to='certificados_psicologos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
    