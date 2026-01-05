from rest_framework import serializers
from gestor.models.medico import Medico
from gestor.models.paciente import Paciente
from gestor.models.turno import Turno

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

    def validate(self, data):
        if Turno.objects.filter(fecha=data.get('fecha'), hora=data.get('hora'), medico=data.get('medico')).exists():
            raise serializers.ValidationError("Ya existe un turno para ese médico en esa fecha y hora.")
        return data