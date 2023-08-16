from django import forms
from .models import Psicologo


class FormPsicologo(forms.ModelForm):
    
    class Meta:
        model = Psicologo
        fields = '__all__'