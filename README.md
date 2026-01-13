# 🏥 Gestor de Turnos Médicos

Sistema integral de gestión de turnos médicos desarrollado con Django 5.2 que ofrece tanto una interfaz web tradicional como una API REST completa para la administración de citas médicas, pacientes y profesionales de la salud.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#️-tecnologías)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Uso](#-uso)
- [API REST](#-api-rest)
- [Modelos de Datos](#-modelos-de-datos)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Testing](#-testing)
- [Despliegue](#-despliegue)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

### Funcionalidades Principales

- **Gestión de Turnos**: Creación, consulta, actualización y eliminación de citas médicas
- **Prevención de Conflictos**: Sistema que previene la reserva duplicada de turnos (mismo médico/fecha/hora)
- **Gestión de Pacientes**: Registro y administración completa de información de pacientes
- **Gestión de Médicos**: Control de profesionales médicos con número de matrícula
- **Especialidades Médicas**: Soporte para múltiples especialidades
- **Control de Cobertura**: Gestión de obras sociales y seguros médicos
- **Interfaz Web**: Panel web intuitivo para gestión de turnos
- **API REST**: API completa con autenticación JWT para integración con aplicaciones externas
- **Filtrado Avanzado**: Búsqueda y filtrado por fecha, hora, médico, paciente, especialidad y cobertura
- **Autenticación Segura**: Sistema de autenticación con JWT y sesiones

### Especialidades Soportadas

- Cardiología
- Clínico
- Ginecología
- Neurología
- Oftalmología
- Gastroenterología

## 🛠️ Tecnologías

### Backend

- **Django 5.2**: Framework web de alto nivel
- **Django REST Framework 3.16.1**: Toolkit para construir APIs REST
- **djangorestframework-simplejwt 5.5.1**: Autenticación JWT
- **django-filter 25.1**: Filtrado avanzado de QuerySets
- **django-cors-headers 4.9.0**: Manejo de CORS para APIs

### Frontend

- **Bootstrap 5**: Framework CSS para diseño responsivo
- **django-crispy-forms 2.4**: Renderizado elegante de formularios
- **crispy-bootstrap5 2025.4**: Integración de Crispy Forms con Bootstrap 5
- **django-widget-tweaks 1.5.0**: Personalización de widgets en templates

### Base de Datos

- **SQLite3**: Base de datos por defecto (recomendado PostgreSQL para producción)
- **Django ORM**: Mapeo objeto-relacional

### Utilidades

- **Pillow 11.2.1**: Procesamiento de imágenes
- **python-dateutil 2.9.0**: Utilidades para manejo de fechas
- **pytz 2025.2**: Soporte de zonas horarias
- **python-decouple 3.8**: Gestión de configuración mediante variables de entorno

## 📦 Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd gestor_turnos_proyecto
```

### 2. Crear y Activar Entorno Virtual

**En Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**En Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

```bash
python manage.py migrate
```

### 5. Crear Superusuario (Administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para configurar usuario y contraseña del administrador.

### 6. Iniciar Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`

## ⚙️ Configuración

### Variables de Entorno (Opcional)

Para entornos de producción, se recomienda usar variables de entorno. Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Configuración de CORS

Por defecto, el proyecto acepta peticiones CORS desde:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

Para modificar los orígenes permitidos, edita `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://tu-frontend.com",
]
```

## 💻 Uso

### Interfaz Web

#### Acceso

- **Panel de administración Django**: `http://127.0.0.1:8000/admin/`
- **Lista de turnos**: `http://127.0.0.1:8000/`
- **Crear turno**: `http://127.0.0.1:8000/turno/create/`
- **Detalle de turno**: `http://127.0.0.1:8000/turno/<id>/`

#### Flujo de Trabajo

1. Accede al admin panel y crea médicos iniciales
2. Los pacientes se pueden crear desde el admin o mediante formularios
3. Crea turnos desde `/turno/create/` especificando:
   - Paciente (DNI y nombre)
   - Médico (número de matrícula)
   - Fecha y hora
   - Especialidad
   - Cobertura médica
   - Saldo
   - Observaciones

## 🌐 API REST

### Autenticación

La API utiliza JWT (JSON Web Tokens) para autenticación.

#### Obtener Token

```bash
POST /api/token/
Content-Type: application/json

{
  "username": "tu-usuario",
  "password": "tu-contraseña"
}
```

**Respuesta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Refrescar Token

```bash
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "tu-refresh-token"
}
```

#### Usar Token

Incluye el token de acceso en el header de tus peticiones:

```bash
Authorization: Bearer <access-token>
```

### Endpoints

#### Médicos

| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/api/medicos/` | Listar todos los médicos | Admin |
| POST | `/api/medicos/` | Crear nuevo médico | Admin |
| GET | `/api/medicos/{matricula}/` | Obtener detalle de médico | Admin |
| PUT/PATCH | `/api/medicos/{matricula}/` | Actualizar médico | Admin |
| DELETE | `/api/medicos/{matricula}/` | Eliminar médico | Admin |
| GET | `/api/medicos/{matricula}/turnos/` | Obtener turnos de un médico | Admin |

**Ejemplo - Crear Médico:**
```bash
POST /api/medicos/
Authorization: Bearer <token>
Content-Type: application/json

{
  "num_matricula": "MP12345",
  "nombre": "Dr. Juan Pérez",
  "dni": 12345678,
  "contacto": "juan.perez@hospital.com"
}
```

#### Pacientes

| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/api/pacientes/` | Listar todos los pacientes | Autenticado |
| POST | `/api/pacientes/` | Crear nuevo paciente | Autenticado |
| GET | `/api/pacientes/{dni}/` | Obtener detalle de paciente | Autenticado |
| PUT/PATCH | `/api/pacientes/{dni}/` | Actualizar paciente | Autenticado |
| DELETE | `/api/pacientes/{dni}/` | Eliminar paciente | Autenticado |

**Ejemplo - Crear Paciente:**
```bash
POST /api/pacientes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "dni": 87654321,
  "nombre": "María González",
  "fecha_nac": "1985-05-15",
  "contacto": "maria.gonzalez@email.com"
}
```

#### Turnos

| Método | Endpoint | Descripción | Permisos |
|--------|----------|-------------|----------|
| GET | `/api/turnos/` | Listar todos los turnos | Autenticado |
| POST | `/api/turnos/` | Crear nuevo turno | Autenticado |
| GET | `/api/turnos/{id}/` | Obtener detalle de turno | Autenticado |
| PUT/PATCH | `/api/turnos/{id}/` | Actualizar turno | Autenticado |
| DELETE | `/api/turnos/{id}/` | Eliminar turno | Autenticado |
| GET | `/api/turnos/upcoming/` | Obtener próximos turnos | Autenticado |

**Ejemplo - Crear Turno:**
```bash
POST /api/turnos/
Authorization: Bearer <token>
Content-Type: application/json

{
  "fecha": "2026-02-15",
  "hora": "10:30:00",
  "especialidad": "cardiologia",
  "cobertura": "OSDE",
  "saldo": 5000,
  "observaciones": "Primera consulta",
  "paciente": 87654321,
  "medico": "MP12345"
}
```

### Filtrado y Búsqueda

#### Filtrar Turnos

```bash
GET /api/turnos/?fecha=2026-02-15
GET /api/turnos/?medico=MP12345
GET /api/turnos/?especialidad=cardiologia
GET /api/turnos/?cobertura=OSDE
GET /api/turnos/?saldo__gte=1000
```

#### Buscar por Nombre

```bash
GET /api/turnos/?search=María
GET /api/turnos/?search=Pérez
```

#### Ordenar Resultados

```bash
GET /api/turnos/?ordering=fecha
GET /api/turnos/?ordering=-fecha  # Descendente
GET /api/turnos/?ordering=hora
GET /api/turnos/?ordering=saldo
```

#### Combinación de Filtros

```bash
GET /api/turnos/?fecha=2026-02-15&especialidad=cardiologia&ordering=hora
```

## 📊 Modelos de Datos

### Médico

```python
class Medico(models.Model):
    num_matricula = CharField(max_length=50, primary_key=True)
    nombre = CharField(max_length=200)
    dni = IntegerField()
    contacto = CharField(max_length=200)
```

**Campos:**
- `num_matricula`: Número de matrícula profesional (clave primaria)
- `nombre`: Nombre completo del médico
- `dni`: Documento Nacional de Identidad
- `contacto`: Email o teléfono de contacto

### Paciente

```python
class Paciente(models.Model):
    dni = IntegerField(primary_key=True)
    nombre = CharField(max_length=200)
    fecha_nac = DateField()
    contacto = CharField(max_length=200)
```

**Campos:**
- `dni`: Documento Nacional de Identidad (clave primaria)
- `nombre`: Nombre completo del paciente
- `fecha_nac`: Fecha de nacimiento
- `contacto`: Email o teléfono de contacto

### Turno

```python
class Turno(models.Model):
    id = BigAutoField(primary_key=True)
    fecha = DateField()
    hora = TimeField()
    especialidad = CharField(max_length=200, choices=ESPECIALIDADES)
    cobertura = CharField(max_length=200)
    saldo = IntegerField()
    observaciones = CharField(max_length=500)
    paciente = ForeignKey(Paciente, on_delete=CASCADE)
    medico = ForeignKey(Medico, on_delete=CASCADE)
    
    class Meta:
        unique_together = ['fecha', 'hora', 'medico']
```

**Campos:**
- `id`: Identificador único autogenerado
- `fecha`: Fecha del turno
- `hora`: Hora del turno
- `especialidad`: Especialidad médica (choices predefinidas)
- `cobertura`: Obra social o seguro médico
- `saldo`: Monto pendiente de pago
- `observaciones`: Notas adicionales
- `paciente`: Relación con el paciente
- `medico`: Relación con el médico

**Restricciones:**
- No se permite duplicar turno con mismo médico, fecha y hora

## 📁 Estructura del Proyecto

```
gestor_turnos_proyecto/
├── gestor/                              # Aplicación principal
│   ├── models/                          # Modelos de datos
│   │   ├── __init__.py
│   │   ├── medico.py                    # Modelo Médico
│   │   ├── paciente.py                  # Modelo Paciente
│   │   └── turno.py                     # Modelo Turno
│   ├── api/                             # API REST
│   │   ├── __init__.py
│   │   ├── views.py                     # ViewSets de DRF
│   │   ├── serializers.py               # Serializadores
│   │   ├── urls.py                      # Rutas de API
│   │   ├── filter.py                    # Filtros personalizados
│   │   └── permissions.py               # Permisos personalizados
│   ├── migrations/                      # Migraciones de BD
│   ├── templates/                       # Templates HTML
│   │   └── gestor/
│   │       ├── lista.html
│   │       ├── detalle_turno.html
│   │       └── aniadir_turno.html
│   ├── __init__.py
│   ├── admin.py                         # Configuración admin
│   ├── apps.py                          # Configuración app
│   ├── forms.py                         # Formularios Django
│   ├── urls.py                          # Rutas web
│   └── views.py                         # Vistas web
├── gestor_turnos_proyecto/              # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py                          # Configuración ASGI
│   ├── settings.py                      # Configuración Django
│   ├── urls.py                          # URLs principales
│   └── wsgi.py                          # Configuración WSGI
├── .venv/                               # Entorno virtual (no versionado)
├── db.sqlite3                           # Base de datos (no versionado)
├── manage.py                            # CLI de Django
├── requirements.txt                     # Dependencias Python
└── README.md                            # Este archivo
```

## 🧪 Testing

### Ejecutar Tests

```bash
python manage.py test
```

### Ejecutar Tests con Cobertura

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML en htmlcov/
```

### Crear Datos de Prueba

```bash
python manage.py shell
```

```python
from gestor.models import Medico, Paciente, Turno
from datetime import date, time

# Crear médico
medico = Medico.objects.create(
    num_matricula="MP001",
    nombre="Dr. Carlos Ruiz",
    dni=11223344,
    contacto="carlos.ruiz@hospital.com"
)

# Crear paciente
paciente = Paciente.objects.create(
    dni=99887766,
    nombre="Ana Martínez",
    fecha_nac=date(1990, 3, 20),
    contacto="ana.martinez@email.com"
)

# Crear turno
turno = Turno.objects.create(
    fecha=date(2026, 2, 20),
    hora=time(14, 30),
    especialidad="cardiologia",
    cobertura="Swiss Medical",
    saldo=3000,
    observaciones="Control anual",
    paciente=paciente,
    medico=medico
)
```

## 🚢 Despliegue

### Preparación para Producción

1. **Configurar Variables de Entorno**

```bash
# .env
SECRET_KEY=clave-secreta-muy-segura
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

2. **Actualizar settings.py**

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
```

3. **Cambiar a PostgreSQL (Recomendado)**

```bash
pip install psycopg2-binary
```

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

4. **Configurar Archivos Estáticos**

```bash
python manage.py collectstatic
```

5. **Servidor de Producción (Gunicorn + Nginx)**

```bash
pip install gunicorn
gunicorn gestor_turnos_proyecto.wsgi:application --bind 0.0.0.0:8000
```

### Opciones de Hosting

- **PythonAnywhere**: Ideal para proyectos pequeños
- **Heroku**: Despliegue rápido con PostgreSQL
- **DigitalOcean**: VPS con control total
- **AWS / Google Cloud / Azure**: Escalabilidad empresarial

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guía de Estilo

- Sigue PEP 8 para código Python
- Documenta funciones y clases con docstrings
- Escribe tests para nuevas funcionalidades
- Mantén los commits atómicos y descriptivos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 📞 Contacto y Soporte

Para preguntas, problemas o sugerencias:

- Abre un issue en el repositorio
- Contacta al equipo de desarrollo

## 🙏 Agradecimientos

- Django Software Foundation
- Django REST Framework
- Comunidad de desarrolladores open source

---

Desarrollado con ❤️ para mejorar la gestión de turnos médicos
