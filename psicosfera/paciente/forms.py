from django import forms
from .models import Paciente, SEXO_CHOICES


class FormPaciente(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'
        
        # widgets = {
        #     'nombre': forms.TextInput(
        #         attrs={'class':'form-control','placeholder':'Nombre'}
        #     ),
        #     'clave': forms.TextInput(
        #         attrs={'class':'form-control','placeholder':'Clave materia'}
        #     ),'semestre': forms.Select(
        #         attrs={'class':'form-control','placeholder':'Semestre'}
        #     ),
        #     # 'optativa': forms.CheckboxInput(attrs={'class':'form-control'),
        #     'creditos': forms.NumberInput(
        #         attrs={'class':'form-control','placeholder':'Créditos'}
        #     ),
        # }
