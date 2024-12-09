# forms.py
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['numeroLegajo', 'nombre', 'apellido', 'email', 'telefono', 'estado']
        widgets = {
            'numeroLegajo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese número de legajo'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@mail.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese teléfono'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'numeroLegajo': 'Número de Legajo',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'estado': 'Activo'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Alumno.objects.filter(email=email).exists() and not self.instance.pk:
            raise forms.ValidationError('Este email ya está registrado')
        return email

    def clean_numeroLegajo(self):
        legajo = self.cleaned_data['numeroLegajo']
        if Alumno.objects.filter(numeroLegajo=legajo).exists() and not self.instance.pk:
            raise forms.ValidationError('Este número de legajo ya existe')
        return legajo