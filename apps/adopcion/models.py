# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre =  models.CharField(max_length=50)
    apellidos =  models.CharField(max_length=70)
    edad =  models.IntegerField()
    telefono =  models.CharField(max_length=12)
    email =  models.EmailField()
    domicilio =  models.TextField()
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    tipo = models.CharField(max_length=20)
    aprobar = models.CharField(max_length=5)
    mascotas = models.ManyToManyField('mascota.Mascota', related_name='Mascota', blank=True)

    def __str__(self):
        return '{} {}'.format(self.persona.nombre, self.persona.apellidos)

class PreSolicitud(models.Model):

        check = models.BooleanField(default=False)
  
        nombre =  models.CharField(max_length=50)
        apellidos =  models.CharField(max_length=70)
        edad =  models.IntegerField()
        telefono =  models.CharField(max_length=12)
        email =  models.EmailField()
        domicilio =  models.TextField()


        numero_mascotas = models.IntegerField()
        razones = models.TextField()
        tipo = models.CharField(max_length=20)
        aprobar = models.CharField(max_length=5)
        mascota = models.ManyToManyField('mascota.Mascota', related_name='PreMascota', null=True, blank=True)

    
        nombre_mascota = models.CharField(max_length=50, null=True, blank=True)
        sexo = models.CharField(max_length=10, null=True, blank=True)
        edad_aproximada = models.IntegerField(null=True, blank=True)
        fecha_rescate = models.DateField(null=True, blank=True)
        vacuna = models.ManyToManyField('mascota.Vacuna', related_name='Vacuna', null=True, blank=True)
        foto = models.ImageField(upload_to='Mascotas/', null=True, blank=True)
        especie = models.CharField(max_length=50, null=True, blank=True)
        raza = models.CharField(max_length=50, null=True, blank=True)
        reseña = models.TextField(max_length=580)

        def __str__(self):
            return '{} {}'.format(self.nombre, self.tipo)