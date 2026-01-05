from django.db import models

class Medico(models.Model):
    def __str__(self):
        return self.nombre

    num_matricula = models.CharField(max_length=20, primary_key=True, verbose_name="Número de Matrícula")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    dni = models.IntegerField(verbose_name="DNI")
    contacto = models.CharField(max_length=20, verbose_name="Contacto")
