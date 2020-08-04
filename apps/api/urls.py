from __future__ import unicode_literals
from __future__ import absolute_import 

from rest_framework import routers
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.conf.urls import url, include

from apps.api.viewsets import PersonaViewSet, SolicitudViewSet, PreSolicitudViewSet, PreSolicitudViewSetClient, MascotaViewSet, CategoriaViewSet, VacunaViewSet, NoticiaViewSet

router = routers.SimpleRouter()
# App Adopciòn
router.register(r'adopcion/personas', PersonaViewSet)
router.register(r'adopcion/solicitud', SolicitudViewSet)
router.register(r'adopcion/pre-solicitud-administrar', PreSolicitudViewSet)
router.register(r'adopcion/pre-solicitud', PreSolicitudViewSetClient)

# App Mascota
router.register(r'mascota/all', MascotaViewSet)
router.register(r'mascota/categoria', CategoriaViewSet)
router.register(r'mascota/vacuna', VacunaViewSet)

# App Noticias
router.register(r'noticias', NoticiaViewSet)

app_name = 'api'
urlpatterns = router.urls