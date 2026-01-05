from datetime import date
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from gestor.models.medico import Medico
from gestor.models.paciente import Paciente
from gestor.models.turno import Turno

class TurnoAPITestCase(APITestCase):
    def setUp(self):
        self.medico = Medico.objects.create(num_matricula=134223, nombre="Juansete", dni=23187473, contacto=1123746592)
        self.paciente = Paciente.objects.create(nombre='P', dni=123, fecha_nac='2000-01-01', contacto='123')
        self.url = reverse('api:turno-list')
        self.data = {"medico": self.medico.pk, "paciente": self.paciente.dni, "fecha":"2025-12-01","hora":"09:30:00", "especialidad":"CLÍNICO", "cobertura":"obra", "saldo":0}

    def test_create_turno(self):
        self.user = User.objects.create_user(username='test', password='testpass')
        self.client.login(username='test', password='testpass')
        resp = self.client.post(self.url, self.data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_session_authentication(self):
        resp = self.client.post(self.url, self.data, format='json')
        print("STATUS:", resp.status_code)
        print("DATA:", self.data)
        self.assertIn(resp.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_jwt_authentication(self):
        self.user = User.objects.create_user(username='test', password='testpass')
        self.client.login(username='test', password='testpass')
        token = self.client.post(reverse('api:token_obtain_pair'), {'username': 'test', 'password': 'testpass'}).data['access'] # <-- obtiene el token de autenticación
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}') # <-- añade el token de autenticación en este header
        resp = self.client.post(self.url, self.data, format='json')
        print("STATUS:", resp.status_code)
        print("DATA:", self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_turno_filtering(self):
        self.user = User.objects.create_user(username='test', password='testpass')
        self.client.login(username='test', password='testpass')
        # Crear varios turnos
        Turno.objects.create(medico=self.medico, paciente=self.paciente, fecha="2025-12-01", hora="09:30:00", especialidad="CLÍNICO", cobertura="obra", saldo=0)
        Turno.objects.create(medico=self.medico, paciente=self.paciente, fecha="2025-12-02", hora="10:30:00", especialidad="CLÍNICO", cobertura="obra", saldo=50)
        Turno.objects.create(medico=self.medico, paciente=self.paciente, fecha="2025-12-03", hora="11:30:00", especialidad="CLÍNICO", cobertura="obra", saldo=100)
        
        # Filtrar por fecha
        resp = self.client.get(self.url + '?fecha=2025-12-02')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        
        # Filtrar por saldo mayor o igual a 50
        resp = self.client.get(self.url + '?saldo__gte=50')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

    def test_upcoming_only_returns_today_and_future(self):
        url = reverse('api:turno-upcoming')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY3NjQzMTEyLCJpYXQiOjE3Njc2NDI4MTIsImp0aSI6ImNjYTU4Y2EzMjA4ZDRiNGU4OTJjOWMwOWE2OWE0YzZkIiwidXNlcl9pZCI6IjEifQ.taxuQpkd0KGmrvxchPDQ3opTOOemendoB1q2qVmLf6o')
        resp = self.client.get(url)
        assert resp.status_code == status.HTTP_200_OK
        for item in resp.data.get('results', resp.data):
            assert item['fecha'] >= str(date.today())