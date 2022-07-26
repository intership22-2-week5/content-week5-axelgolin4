from django.contrib import admin

# Register your models here.
from .models import Autor, Obra, Foto, Exposicion

admin.site.register(Autor)
admin.site.register(Obra)
admin.site.register(Foto)
admin.site.register(Exposicion)
