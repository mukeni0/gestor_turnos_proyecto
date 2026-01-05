from django.db import models
from .medico import Medico
from .paciente import Paciente
from datetime import datetime

class Turno(models.Model):
    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.paciente.dni}"

    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")

    @property
    def fecha_hora(self):
        return datetime.combine(self.fecha, self.hora)

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    ESPECIALIDADES = [
        ("CARDIOLOGÍA", "Cardiología"),
        ("CLÍNICO", "Clínico"),
        ("GINECOLOGÍA", "Ginecología"),
        ("NEUROLOGÍA", "Neurología"),
        ("OFTALMOLOGÍA", "Oftalmología"),
        ("GASTROENTEROLOGÍA", "Gastroenterología"),
    ]

    especialidad = models.CharField(
        max_length=30,
        choices=ESPECIALIDADES,
        verbose_name="Especialidad"
    )

    cobertura = models.CharField(max_length=30, verbose_name="Cobertura")
    saldo = models.IntegerField(verbose_name="Saldo")
    observaciones = models.CharField(max_length=200, blank=True, verbose_name="Observaciones")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["fecha", "hora", "medico"], name="unique_turno_por_medico_en_fecha_hora"),
        ]