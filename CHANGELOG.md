# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Añadido en branch mukeni0 - 2026-01-13

#### Documentación
- **README.md completo y detallado**
  - Documentación completa del proyecto con tabla de contenidos
  - Descripción de características y funcionalidades
  - Stack tecnológico con versiones específicas
  - Instrucciones de instalación paso a paso (Linux/macOS/Windows)
  - Guía de configuración con variables de entorno
  - Documentación completa de API REST con ejemplos curl
  - Tabla de endpoints con métodos HTTP y permisos
  - Ejemplos de autenticación JWT
  - Guía de filtrado, búsqueda y ordenamiento de resultados
  - Diagramas de modelos de datos con campos explicados
  - Estructura del proyecto detallada
  - Sección de testing con ejemplos de datos de prueba
  - Guía de despliegue a producción
  - Recomendaciones de hosting
  - Guía de contribución y estilo de código

#### Herramientas de Desarrollo
- **create_test_data.py** - Script para popular la base de datos
  - Creación automática de 5 médicos con diferentes especialidades
  - Generación de 7 pacientes con datos completos
  - Creación de 8 turnos de prueba distribuidos en los próximos días
  - Datos realistas con diferentes especialidades y coberturas
  - Sistema de validación que evita duplicados
  - Reporte detallado de operaciones realizadas

#### Entorno de Desarrollo
- Configuración completa de entorno virtual Python (.venv)
- Instalación automatizada de todas las dependencias
- Base de datos SQLite inicializada con migraciones aplicadas
- Usuario administrador de prueba creado (admin/admin123)

### Corregido en branch mukeni0 - 2026-01-13

#### Modelos
- **gestor/models/__init__.py**
  - Agregados exports explícitos de Medico, Paciente y Turno
  - Soluciona ImportError al importar modelos desde gestor.models
  - Añadido `__all__` para mejorar la claridad de la API del módulo

#### API REST
- **gestor/api/views.py**
  - Agregado import faltante de `Response` desde rest_framework.response
  - Agregado import faltante de `date` desde datetime
  - Corregido error `NameError: name 'date' is not defined` en endpoint upcoming
  - Eliminada duplicación del método `upcoming()` en TurnoViewSet
  - Corregido `TurnoFilter.objects` a `Turno.objects` en MedicoViewSet.turnos()
  - Reorganizados imports siguiendo convenciones de Django (stdlib, terceros, locales)
  - Mejorado formato de código para mayor legibilidad

### Testeado en branch mukeni0 - 2026-01-13

#### Endpoints Verificados
- ✅ `POST /api/token/` - Autenticación JWT funcionando correctamente
- ✅ `GET /api/turnos/` - Listado de turnos con paginación
- ✅ `GET /api/medicos/` - Listado de médicos (requiere admin)
- ✅ `GET /api/pacientes/` - Listado de pacientes
- ✅ `GET /api/turnos/upcoming/` - Próximos turnos ordenados por fecha/hora
- ✅ `GET /` - Interfaz web renderiza correctamente con Bootstrap 5

#### Funcionalidades Validadas
- Sistema de autenticación JWT genera tokens correctamente
- Permisos funcionan (admin para médicos, autenticado para el resto)
- Relaciones ForeignKey entre Turno-Paciente-Medico funcionan
- Datos de prueba se crean sin errores de integridad
- Sistema de unique_constraint previene turnos duplicados

---

## [0.1.0] - 2026-01-13 (Commit inicial)

### Añadido
- Estructura básica del proyecto Django
- Modelos: Medico, Paciente, Turno
- API REST con Django REST Framework
- Serializers para todos los modelos
- ViewSets con permisos básicos
- Sistema de filtrado con django-filter
- Autenticación JWT con simplejwt
- Soporte CORS para desarrollo frontend
- Templates HTML con Bootstrap 5
- Formularios Django para creación de turnos
- Vistas web tradicionales (lista, detalle, crear)
- Panel de administración Django configurado
- Migraciones de base de datos
- requirements.txt con todas las dependencias

### Características Iniciales
- 6 especialidades médicas soportadas
- Prevención de doble reserva de turnos
- Relaciones entre médicos, pacientes y turnos
- Interfaz web básica funcional
- API REST completa con CRUD

---

## Tipos de Cambios

- **Añadido**: para nuevas funcionalidades
- **Cambiado**: para cambios en funcionalidades existentes
- **Obsoleto**: para funcionalidades que serán eliminadas
- **Eliminado**: para funcionalidades eliminadas
- **Corregido**: para corrección de bugs
- **Seguridad**: para vulnerabilidades de seguridad

---

## Notas de Versión

### [Unreleased] - Branch mukeni0
Esta versión incluye mejoras significativas en documentación, herramientas de desarrollo y correcciones críticas de bugs que impedían el funcionamiento correcto de la API. Todos los endpoints han sido testeados y verificados. El proyecto está listo para desarrollo activo.

**Breaking Changes**: Ninguno

**Migraciones Requeridas**: No

**Notas de Actualización**: 
- Si actualizas desde main, necesitarás ejecutar `python manage.py migrate`
- Se recomienda crear un nuevo entorno virtual y reinstalar dependencias
- Usa el script `create_test_data.py` para popular la base de datos con datos de prueba

### [0.1.0] - Versión Inicial
Primera versión funcional del sistema de gestión de turnos médicos con Django y API REST completa.
