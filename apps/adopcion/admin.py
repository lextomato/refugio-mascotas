from django.contrib import admin

from apps.adopcion.models import Persona, Solicitud, PreSolicitud

# Register your models here.
admin.site.register(Persona)
admin.site.register(Solicitud)
admin.site.register(PreSolicitud)
