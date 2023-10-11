from django import forms
from .models import Psicologo,Consultorio


class FormPsicologo(forms.ModelForm):
    
    class Meta:
        model = Psicologo
        fields = '__all__'
        
        widgets = {
            'user': forms.TextInput(
                attrs={'class':'form-control'}
            ),
           'especialidad': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'especialidad-input'}
            ),
        }

class FormConsultorio(forms.ModelForm):
    
    class Meta:
        model = Consultorio
        fields = '__all__'
        
        widgets = {
            'direccion': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'direccion-input'}
            ),
        }