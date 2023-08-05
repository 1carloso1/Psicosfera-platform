from django.contrib import admin
from .models import Psicologo, Paciente, Cita, Expediente

# Register your models here.
admin.register(Psicologo)
admin.register(Paciente)
admin.register(Cita)
admin.register(Expediente)
