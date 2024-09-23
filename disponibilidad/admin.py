from django.contrib import admin
from .models import docente, estudiante, disponibilidad, estado_solicitud, solicitud 
# Register your models here.
admin.site.register(docente)
admin.site.register(estudiante)
admin.site.register(disponibilidad)
admin.site.register(estado_solicitud)
admin.site.register(solicitud)