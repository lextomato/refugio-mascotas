from rest_framework import serializers
from apps.adopcion.models import Persona, Solicitud, PreSolicitud

# App Adopción

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('__all__')

class SolicitudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Solicitud
        fields = '__all__'

class PreSolicitudSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PreSolicitud
        fields = '__all__'


# App Mascota
from apps.mascota.models import Mascota, Categoria, Vacuna

class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class VacunaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vacuna
        fields = '__all__'


# App Noticias
from apps.noticias.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticia
        fields = ('__all__')
