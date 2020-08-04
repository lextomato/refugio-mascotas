from __future__ import unicode_literals
from __future__ import absolute_import

from django import forms
from django.forms import ModelForm
from apps.mascota.models import Mascota, Categoria

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'foto',
            'categoria',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
            'foto': 'Foto',
            'categoria': 'Categoría de la Mascota',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }
