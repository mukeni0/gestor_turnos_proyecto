from django.contrib import admin
from .models.medico import Medico
from .models.paciente import Paciente
from .models.turno import Turno

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Turno)