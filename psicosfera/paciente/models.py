from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Modelo de paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=120, verbose_name="Primer Apellido")
    amaterno= models.CharField(max_length=120, verbose_name="Segundo Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    ocupacion = models.CharField(max_length=100, verbose_name="Ocupación")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200, blank=True, verbose_name="Dirección")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='pacientes_foto_perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo de expedinte de un pacinte
class Expediente(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    antecedentes_medicos = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Expediente #{self.num_expediente} - Paciente: {self.paciente.nombre}"

    