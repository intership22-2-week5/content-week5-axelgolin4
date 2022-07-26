from django.contrib import admin

# Register your models here.
from .models import Raton, Teclado, Monitor, Computadora, Orden

admin.site.register(Raton)
admin.site.register(Teclado)
admin.site.register(Monitor)
admin.site.register(Computadora)
admin.site.register(Orden)