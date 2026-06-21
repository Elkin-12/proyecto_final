from django import forms
from .models import Cita, Servicio

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['cliente', 'medico', 'servicio', 'fecha_hora', 'estado']
        
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'fecha_hora': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local',
                'style': 'border-radius: 12px; border-color: #e2e8f0; height: 48px;'
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control ps-3',
                'placeholder': 'Ej. Consulta General, Radiografía...',
                'style': 'border-radius: 12px; border-color: #e2e8f0; height: 48px; background-color: #f8fafc;'
            }),
        }