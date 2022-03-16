from django.contrib import admin

# Register your models here.

from .models import doctor,client

admin.site.register(doctor)
admin.site.register(client)