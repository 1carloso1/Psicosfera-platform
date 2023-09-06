from django import forms
from .models import Paciente, SEXO_CHOICES


class FormPaciente(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'
        
        widgets = {
            'user': forms.TextInput(
                attrs={'class':'form-control'}
            ),
        }
