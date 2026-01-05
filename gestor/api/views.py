from argparse import Action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from gestor.models.medico import Medico
from gestor.models.paciente import Paciente
from gestor.models.turno import Turno
from .serializers import MedicoSerializer, PacienteSerializer, TurnoSerializer
from .filter import TurnoFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path='turnos')
    def turnos(self, request, pk=None):
        medico = self.get_object()
        turnos = TurnoFilter.objects.filter(medico=medico)
        page = self.paginate_queryset(turnos)
        if page is not None:
            serializer = TurnoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.select_related('medico','paciente').all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TurnoFilter
    search_fields = ['paciente__nombre','medico__nombre']
    ordering_fields = ['fecha','hora','saldo']

    def perform_create(self, serializer):
        # no asignamos paciente desde request.user; dejamos que envíe el paciente (ID)
        serializer.save()

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        # 1) Filtrar por fecha >= hoy y aplicar filtros/search/order que ya esten
        qs = self.filter_queryset(self.get_queryset().filter(fecha__gte=date.today()).order_by('fecha', 'hora'))
        # 2) Paginación si aplica
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # 3) Respuesta no paginada
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)