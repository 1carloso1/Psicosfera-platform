from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

ESPECIALIDADES_CHOICES = (
    ('clinica', 'Psicología Clínica'),
    ('educativa', 'Psicología Educativa'),
    ('deporte', 'Psicología del Deporte'),
    ('organizacional', 'Psicología Organizacional'),
    ('forense', 'Psicología Forense'),
    ('salud_mental', 'Salud Mental'),
    ('terapia_familiar', 'Terapia Familiar'),
    ('neuropsicologia', 'Neuropsicología'),
    ('psicologia_infantil', 'Psicología Infantil'),
    ('psicoterapia', 'Psicoterapia'),
    ('psicologia_social', 'Psicología Social'),
    ('gerontologia', 'Gerontología'),
    ('psicologia_rehabilitacion', 'Psicología de la Rehabilitación'),
    ('psicologia_educacional', 'Psicología Educacional'),
    ('psicologia_legal', 'Psicología Legal'),
    ('orientacion_vocacional', 'Orientación Vocacional'),
    ('terapia_sexual', 'Terapia Sexual'),
    ('terapia_pareja', 'Terapia de Pareja'),
    ('psicologia_transpersonal', 'Psicología Transpersonal'),
    # Agrega más especialidaes si es necesario
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
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=120, verbose_name="Primer Apellido")
    amaterno= models.CharField(max_length=120, verbose_name="Segundo Apellido")
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField(null=True, verbose_name="Fecha de nacimiento")
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDADES_CHOICES)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    institucion_otorgamiento = models.CharField(max_length=200, blank=True, null=True, verbose_name="Institución de otorgamiento")
    anio_obtencion = models.PositiveIntegerField(null=True, verbose_name="Año de obtención")
    metodo_pago = models.CharField(max_length=100, choices=METODOS_PAGO_CHOICES, blank=True, null=True)
    curriculum = models.FileField(upload_to='curriculum_psicologo/', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='psicologos_foto_perfil/', blank=True, null=True)
    certificado = models.FileField(upload_to='certificados_psicologos/', blank=True, null=True)
    identificacion_oficial = models.FileField(upload_to='identificacion_psicologos/', blank=True, null=True) 
    enlace_pagina_web = models.URLField(blank=True)
    enlace_facebook = models.URLField(blank=True)
    enlace_instagram = models.URLField(blank=True)
    enlace_linkedin = models.URLField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    consultorio = models.ForeignKey('Consultorio', verbose_name='Consultorio', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# Modelo de consultorio de los psicologos
class Consultorio(models.Model):
    direccion = models.CharField(max_length=200, blank=True)
    horario_atencion = models.CharField(max_length=200, blank=True)
    servicios_ofrecidos = models.TextField(blank=True)

    def __str__(self):
        return f"Consultorio en {self.direccion}"

    