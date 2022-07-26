from django.contrib import admin

# Register your models here.
from .models import Keyboard, Mouse, Display, Speaker, Computer

admin.site.register(Keyboard)
admin.site.register(Mouse)
admin.site.register(Display)
admin.site.register(Speaker)
admin.site.register(Computer)