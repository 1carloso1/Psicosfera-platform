from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

ESTATUS_CHOICES = (
    ('P', 'Previa'),
    ('PR', 'Próxima'),
    ('PN', 'Pendiente'),
    ('H', 'Hecha'),
)

# Modelo de psicologo
class Psicologo(models.Model):
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=120)
    amaterno= models.CharField(max_length=120)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    especialidad = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    ubicacion = models.TextField()
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto_perfil = models.ImageField(upload_to='psicologos/', blank=True, null=True)
    certificado_pdf = models.FileField(upload_to='certificados/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

# Modelo de paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=120)
    amaterno= models.CharField(max_length=120)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    ocupacion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

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
  
# Modelo de cita
class Cita(models.Model):
    folio_cita = models.CharField(primary_key=True, max_length=10)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    psicologo = models.ForeignKey('Psicologo', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(max_length=200)
    notas = models.TextField()
    estatus = models.CharField(max_length=2, choices=ESTATUS_CHOICES, default='PN') 
    costo = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.paciente.nombre} - {self.psicologo.nombre}"    
    
