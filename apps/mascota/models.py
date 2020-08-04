# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import 

from django.db import models

from apps.adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Categoria(models.Model):
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.especie, self.raza)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, related_name='adoptante', null=True, blank=True, on_delete=models.CASCADE)
    padrino = models.ForeignKey(Persona, related_name='padrino', null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)
    foto = models.ImageField(upload_to='Mascotas/')
    categoria = models.ManyToManyField(Categoria, blank=True, related_name='categoria')
    reseña = models.TextField(max_length=580)

    def __str__(self):
        return '{}'.format(self.nombre)
