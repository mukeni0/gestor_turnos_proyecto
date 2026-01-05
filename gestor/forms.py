from django import forms
from .models.turno import Turno
from .models.paciente import Paciente
from .models.medico import Medico

class TurnosForm(forms.ModelForm):
    class Meta:
        model = Turno
        exclude = ['paciente', 'medico']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
            'cobertura': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['dni', 'nombre', 'fecha_nac', 'contacto']
        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['num_matricula', 'nombre', 'dni', 'contacto']
        widgets = {
            'num_matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }