from __future__ import unicode_literals
from __future__ import absolute_import

from django import forms
from django.forms import ModelForm
from apps.noticias.models import Noticia, AlbumImagenes

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia

        fields = [
            'Creador',
            'titulo',
            'categoria',
            'contenido',
            'img_portada',
        ]
        labels = {
            'Creador': 'Creador',
            'titulo': 'Titulo de noticia',
            'categoria': 'Categoria de la noticia',
            'contenido': 'Contenido',
            'img_portada': 'Imagen de portada',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'img_portada': forms.FileInput(attrs={'class':'form-control'}),
        }

class AlbumImagenesForm(forms.ModelForm):

    class Meta:
        model = AlbumImagenes

        fields = [
            'imagenes',
        ]
        labels = {
            'imagenes': 'Imagenes',
        }
