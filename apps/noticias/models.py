# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Noticia(models.Model):
    Creador = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    titulo =  models.CharField(max_length=100)
    categoria =  models.CharField(max_length=20)
    contenido =  RichTextField()
    img_portada = models.ImageField(upload_to='Noticias/')
    fecha =  models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.titulo)


class AlbumImagenes(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.DO_NOTHING, null=True, blank=True)
    imagenes = models.ImageField(upload_to='Noticias/')

