from django.contrib import admin

from apps.noticias.models import Noticia, AlbumImagenes

# Register your models here.
admin.site.register(Noticia)
admin.site.register(AlbumImagenes)