from django import forms
from .models import Medico, Especialidad

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Alejandro'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Peralta'}),
            'especialidad': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Cardiología'}),
        }