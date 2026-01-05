import django_filters
from gestor.models.turno import Turno 

class TurnoFilter(django_filters.FilterSet):

    class Meta:
        model = Turno
        fields = {
            'fecha': ['exact', 'gte', 'lte'],
            'hora': ['exact', 'gte', 'lte'],
            'medico': ['exact'],
            'paciente': ['exact'],
            'especialidad': ['exact'],
            'cobertura': ['exact'],
            'saldo': ['exact', 'gte', 'lte'],
        }