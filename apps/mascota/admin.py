# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from apps.mascota.models import Vacuna, Mascota, Categoria

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)
admin.site.register(Categoria)