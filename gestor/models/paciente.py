from django.db import models

class Paciente(models.Model):
    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    dni = models.IntegerField(primary_key=True, verbose_name="DNI")
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    contacto = models.CharField(max_length=20, verbose_name="Contacto")
