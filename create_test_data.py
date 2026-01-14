"""
Script para crear datos de prueba en el sistema de gestión de turnos
"""

import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestor_turnos_proyecto.settings")
django.setup()

from gestor.models import Medico, Paciente, Turno
from datetime import date, time, timedelta


def create_test_data():
    print("Creando datos de prueba...")

    # Crear médicos
    medicos_data = [
        {
            "num_matricula": "MP12345",
            "nombre": "Dr. Juan Carlos Pérez",
            "dni": 20123456,
            "contacto": "jperez@hospital.com",
        },
        {
            "num_matricula": "MP67890",
            "nombre": "Dra. María Laura González",
            "dni": 25678901,
            "contacto": "mgonzalez@clinica.com",
        },
        {
            "num_matricula": "MP11111",
            "nombre": "Dr. Roberto Fernández",
            "dni": 18222333,
            "contacto": "rfernandez@medico.com",
        },
        {
            "num_matricula": "MP22222",
            "nombre": "Dra. Ana Martínez",
            "dni": 22333444,
            "contacto": "amartinez@hospital.com",
        },
        {
            "num_matricula": "MP33333",
            "nombre": "Dr. Carlos Rodríguez",
            "dni": 19444555,
            "contacto": "crodriguez@clinica.com",
        },
    ]

    for medico_data in medicos_data:
        medico, created = Medico.objects.get_or_create(
            num_matricula=medico_data["num_matricula"], defaults=medico_data
        )
        if created:
            print(f"✓ Médico creado: {medico.nombre}")
        else:
            print(f"- Médico ya existe: {medico.nombre}")

    # Crear pacientes
    pacientes_data = [
        {
            "dni": 30123456,
            "nombre": "Pedro García",
            "fecha_nac": date(1985, 3, 15),
            "contacto": "pedro.garcia@email.com",
        },
        {
            "dni": 35678901,
            "nombre": "Laura Sánchez",
            "fecha_nac": date(1990, 7, 22),
            "contacto": "laura.sanchez@email.com",
        },
        {
            "dni": 28111222,
            "nombre": "Miguel Torres",
            "fecha_nac": date(1978, 11, 5),
            "contacto": "miguel.torres@email.com",
        },
        {
            "dni": 32333444,
            "nombre": "Carolina López",
            "fecha_nac": date(1995, 2, 18),
            "contacto": "carolina.lopez@email.com",
        },
        {
            "dni": 27444555,
            "nombre": "Javier Ramírez",
            "fecha_nac": date(1982, 9, 30),
            "contacto": "javier.ramirez@email.com",
        },
        {
            "dni": 33555666,
            "nombre": "Sofía Morales",
            "fecha_nac": date(1988, 6, 12),
            "contacto": "sofia.morales@email.com",
        },
        {
            "dni": 29666777,
            "nombre": "Diego Castro",
            "fecha_nac": date(1975, 4, 25),
            "contacto": "diego.castro@email.com",
        },
    ]

    for paciente_data in pacientes_data:
        paciente, created = Paciente.objects.get_or_create(
            dni=paciente_data["dni"], defaults=paciente_data
        )
        if created:
            print(f"✓ Paciente creado: {paciente.nombre}")
        else:
            print(f"- Paciente ya existe: {paciente.nombre}")

    # Crear turnos
    especialidades = [
        "cardiologia",
        "clinico",
        "ginecologia",
        "neurologia",
        "oftalmologia",
        "gastroenterologia",
    ]
    coberturas = ["OSDE", "Swiss Medical", "Galeno", "OSECAC", "IOMA", "Particular"]

    turnos_data = [
        {
            "fecha": date.today() + timedelta(days=1),
            "hora": time(9, 0),
            "especialidad": "cardiologia",
            "cobertura": "OSDE",
            "saldo": 5000,
            "observaciones": "Primera consulta - Control de presión",
            "paciente_dni": 30123456,
            "medico_matricula": "MP12345",
        },
        {
            "fecha": date.today() + timedelta(days=1),
            "hora": time(10, 30),
            "especialidad": "clinico",
            "cobertura": "Swiss Medical",
            "saldo": 3000,
            "observaciones": "Chequeo anual",
            "paciente_dni": 35678901,
            "medico_matricula": "MP67890",
        },
        {
            "fecha": date.today() + timedelta(days=2),
            "hora": time(14, 0),
            "especialidad": "neurologia",
            "cobertura": "Galeno",
            "saldo": 7000,
            "observaciones": "Consulta por migrañas",
            "paciente_dni": 28111222,
            "medico_matricula": "MP11111",
        },
        {
            "fecha": date.today() + timedelta(days=2),
            "hora": time(16, 30),
            "especialidad": "oftalmologia",
            "cobertura": "OSECAC",
            "saldo": 4500,
            "observaciones": "Control de vista",
            "paciente_dni": 32333444,
            "medico_matricula": "MP22222",
        },
        {
            "fecha": date.today() + timedelta(days=3),
            "hora": time(11, 0),
            "especialidad": "gastroenterologia",
            "cobertura": "IOMA",
            "saldo": 6000,
            "observaciones": "Gastritis - seguimiento",
            "paciente_dni": 27444555,
            "medico_matricula": "MP33333",
        },
        {
            "fecha": date.today() + timedelta(days=3),
            "hora": time(15, 0),
            "especialidad": "cardiologia",
            "cobertura": "Particular",
            "saldo": 8000,
            "observaciones": "Control post-operatorio",
            "paciente_dni": 33555666,
            "medico_matricula": "MP12345",
        },
        {
            "fecha": date.today() + timedelta(days=4),
            "hora": time(9, 30),
            "especialidad": "clinico",
            "cobertura": "OSDE",
            "saldo": 3500,
            "observaciones": "Análisis de resultados",
            "paciente_dni": 29666777,
            "medico_matricula": "MP67890",
        },
        {
            "fecha": date.today() + timedelta(days=5),
            "hora": time(13, 0),
            "especialidad": "neurologia",
            "cobertura": "Swiss Medical",
            "saldo": 7500,
            "observaciones": "Segunda consulta - evolución positiva",
            "paciente_dni": 28111222,
            "medico_matricula": "MP11111",
        },
    ]

    turnos_creados = 0
    for turno_data in turnos_data:
        try:
            paciente = Paciente.objects.get(dni=turno_data.pop("paciente_dni"))
            medico = Medico.objects.get(
                num_matricula=turno_data.pop("medico_matricula")
            )

            turno, created = Turno.objects.get_or_create(
                fecha=turno_data["fecha"],
                hora=turno_data["hora"],
                medico=medico,
                defaults={**turno_data, "paciente": paciente},
            )

            if created:
                print(
                    f"✓ Turno creado: {turno.fecha} {turno.hora} - {paciente.nombre} con {medico.nombre}"
                )
                turnos_creados += 1
            else:
                print(f"- Turno ya existe: {turno.fecha} {turno.hora}")
        except Exception as e:
            print(f"✗ Error creando turno: {e}")

    print("\n" + "=" * 60)
    print("Resumen:")
    print(f"Total médicos: {Medico.objects.count()}")
    print(f"Total pacientes: {Paciente.objects.count()}")
    print(f"Total turnos: {Turno.objects.count()}")
    print(f"Turnos creados en esta ejecución: {turnos_creados}")
    print("=" * 60)


if __name__ == "__main__":
    print("="*60)

if __name__ == '__main__':
    create_test_data()
    print("\n¡Datos de prueba creados exitosamente!")
