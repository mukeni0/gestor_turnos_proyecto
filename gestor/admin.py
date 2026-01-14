from django.contrib import admin
from django.db.models import Q
from django.utils.html import format_html

from .models.medico import Medico
from .models.paciente import Paciente
from .models.turno import Turno


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    """Administración de Médicos con búsqueda y filtros"""

    list_display = ["num_matricula", "nombre", "dni", "contacto", "cantidad_turnos"]
    list_display_links = ["num_matricula", "nombre"]
    search_fields = ["num_matricula", "nombre", "dni", "contacto"]
    ordering = ["nombre"]
    list_per_page = 25

    fieldsets = (
        ("Información Profesional", {"fields": ("num_matricula", "nombre")}),
        ("Información Personal", {"fields": ("dni", "contacto")}),
    )

    def cantidad_turnos(self, obj):
        """Muestra la cantidad de turnos asignados al médico"""
        count = obj.turno_set.count()
        if count > 0:
            return format_html(
                '<span style="color: green; font-weight: bold;">{} turnos</span>', count
            )
        return format_html('<span style="color: gray;">Sin turnos</span>')

    cantidad_turnos.short_description = "Turnos Asignados"

    def get_queryset(self, request):
        """Optimiza la query para evitar N+1"""
        qs = super().get_queryset(request)
        return qs.prefetch_related("turno_set")


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    """Administración de Pacientes con información detallada"""

    list_display = ["dni", "nombre", "edad", "fecha_nac", "contacto", "cantidad_turnos"]
    list_display_links = ["dni", "nombre"]
    search_fields = ["dni", "nombre", "contacto"]
    list_filter = ["fecha_nac"]
    ordering = ["nombre"]
    list_per_page = 25
    date_hierarchy = "fecha_nac"

    fieldsets = (
        ("Información Personal", {"fields": ("dni", "nombre", "fecha_nac")}),
        ("Contacto", {"fields": ("contacto",)}),
    )

    def edad(self, obj):
        """Calcula y muestra la edad del paciente"""
        from datetime import date

        today = date.today()
        age = (
            today.year
            - obj.fecha_nac.year
            - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        )
        return f"{age} años"

    edad.short_description = "Edad"
    edad.admin_order_field = "fecha_nac"

    def cantidad_turnos(self, obj):
        """Muestra la cantidad de turnos del paciente"""
        count = obj.turno_set.count()
        if count > 0:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{} turnos</span>', count
            )
        return format_html('<span style="color: gray;">Sin turnos</span>')

    cantidad_turnos.short_description = "Turnos Registrados"

    def get_queryset(self, request):
        """Optimiza la query para evitar N+1"""
        qs = super().get_queryset(request)
        return qs.prefetch_related("turno_set")


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    """Administración completa de Turnos con filtros y acciones"""

    list_display = [
        "id",
        "fecha",
        "hora",
        "paciente_info",
        "medico_info",
        "especialidad_badge",
        "cobertura",
        "saldo_display",
        "estado_turno",
    ]
    list_display_links = ["id", "fecha"]
    list_filter = [
        "especialidad",
        "fecha",
        "cobertura",
        "medico",
    ]
    search_fields = [
        "paciente__nombre",
        "paciente__dni",
        "medico__nombre",
        "medico__num_matricula",
        "observaciones",
    ]
    date_hierarchy = "fecha"
    ordering = ["-fecha", "-hora"]
    list_per_page = 30

    autocomplete_fields = ["paciente", "medico"]

    fieldsets = (
        (
            "Fecha y Hora",
            {"fields": ("fecha", "hora"), "description": "Programación del turno"},
        ),
        (
            "Participantes",
            {
                "fields": ("paciente", "medico", "especialidad"),
            },
        ),
        (
            "Información Administrativa",
            {
                "fields": ("cobertura", "saldo"),
            },
        ),
        (
            "Observaciones",
            {
                "fields": ("observaciones",),
                "classes": ("collapse",),
            },
        ),
    )

    actions = ["marcar_pagado", "exportar_turnos"]

    def paciente_info(self, obj):
        """Muestra información del paciente con formato"""
        return format_html(
            "<strong>{}</strong><br><small>DNI: {}</small>",
            obj.paciente.nombre,
            obj.paciente.dni,
        )

    paciente_info.short_description = "Paciente"

    def medico_info(self, obj):
        """Muestra información del médico con formato"""
        return format_html(
            "<strong>{}</strong><br><small>Mat: {}</small>",
            obj.medico.nombre,
            obj.medico.num_matricula,
        )

    medico_info.short_description = "Médico"

    def especialidad_badge(self, obj):
        """Muestra la especialidad con colores"""
        colores = {
            "CARDIOLOGÍA": "#e74c3c",
            "CLÍNICO": "#3498db",
            "GINECOLOGÍA": "#e91e63",
            "NEUROLOGÍA": "#9b59b6",
            "OFTALMOLOGÍA": "#f39c12",
            "GASTROENTEROLOGÍA": "#27ae60",
        }
        color = colores.get(obj.especialidad, "#95a5a6")
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.get_especialidad_display(),
        )

    especialidad_badge.short_description = "Especialidad"
    especialidad_badge.admin_order_field = "especialidad"

    def saldo_display(self, obj):
        """Muestra el saldo con formato de moneda y color"""
        if obj.saldo == 0:
            color = "green"
            texto = "PAGADO"
        elif obj.saldo < 0:
            color = "red"
            texto = f"${abs(obj.saldo):,}"
        else:
            color = "orange"
            texto = f"${obj.saldo:,}"

        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>', color, texto
        )

    saldo_display.short_description = "Saldo"
    saldo_display.admin_order_field = "saldo"

    def estado_turno(self, obj):
        """Muestra el estado del turno (pasado/futuro)"""
        from datetime import date, datetime, time

        hoy = date.today()
        ahora = datetime.now().time()

        if obj.fecha < hoy or (obj.fecha == hoy and obj.hora < ahora):
            return format_html(
                '<span style="background-color: #95a5a6; color: white; padding: 2px 8px; '
                'border-radius: 3px; font-size: 10px;">PASADO</span>'
            )
        elif obj.fecha == hoy:
            return format_html(
                '<span style="background-color: #e67e22; color: white; padding: 2px 8px; '
                'border-radius: 3px; font-size: 10px;">HOY</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #27ae60; color: white; padding: 2px 8px; '
                'border-radius: 3px; font-size: 10px;">PRÓXIMO</span>'
            )

    estado_turno.short_description = "Estado"

    def marcar_pagado(self, request, queryset):
        """Acción para marcar turnos como pagados (saldo = 0)"""
        updated = queryset.update(saldo=0)
        self.message_user(request, f"{updated} turno(s) marcado(s) como pagado(s).")

    marcar_pagado.short_description = "Marcar como pagado"

    def exportar_turnos(self, request, queryset):
        """Acción para exportar turnos (placeholder para futuro)"""
        self.message_user(
            request,
            f"{queryset.count()} turno(s) seleccionado(s) para exportar. "
            "Funcionalidad en desarrollo.",
        )

    exportar_turnos.short_description = "Exportar turnos seleccionados"

    def get_queryset(self, request):
        """Optimiza queries con select_related"""
        qs = super().get_queryset(request)
        return qs.select_related("paciente", "medico")


# Personalización del sitio de administración
admin.site.site_header = "Gestor de Turnos Médicos - Administración"
admin.site.site_title = "Gestor de Turnos"
admin.site.index_title = "Panel de Administración"
