from django.contrib import admin
from .models import Service

# Registro o serviço para aparecer no painel
admin.site.register(Service)