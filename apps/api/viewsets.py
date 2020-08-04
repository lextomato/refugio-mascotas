from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import viewsets
from rest_framework import mixins


# App Adopción
from apps.adopcion.models import Persona, Solicitud, PreSolicitud
from apps.api.serializer import PersonaSerializer, SolicitudSerializer, PreSolicitudSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    # authentication_class = (JSONWebTokenAuthentication,) # Don't forget to add a 'comma' after first element to make it a tuple
    # permission_classes = (IsAuthenticated,)
    
    permission_classes = (IsAuthenticated,)
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class PreSolicitudViewSetClient(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = ()
    queryset = PreSolicitud.objects.all()
    serializer_class = PreSolicitudSerializer

class PreSolicitudViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = (IsAuthenticated,)
    queryset = PreSolicitud.objects.all()
    serializer_class = PreSolicitudSerializer


#  App Mascota
from apps.mascota.models import Mascota, Categoria, Vacuna
from apps.api.serializer import MascotaSerializer, CategoriaSerializer, VacunaSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer


# App Noticias 
from apps.noticias.models import Noticia
from apps.api.serializer import NoticiaSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # def get(self, request, format=None):
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer