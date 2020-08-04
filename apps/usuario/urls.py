from __future__ import unicode_literals
from __future__ import absolute_import 

from django.conf.urls import url, include
from django.urls import path

from apps.usuario.views import RegistroUsuario

app_name = 'usuario'
urlpatterns = [
    path(r'registrar/', RegistroUsuario.as_view(), name='registrar'),
]
