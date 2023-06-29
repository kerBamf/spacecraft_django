from django.contrib import admin
from .models import Manufacturer, Spacecraft, Squadron

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Spacecraft)
admin.site.register(Squadron)