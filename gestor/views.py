from django.shortcuts import render, get_object_or_404, redirect
from gestor.models.turno import Turno
from gestor.models.paciente import Paciente
from gestor.models.medico import Medico
from .forms import TurnosForm, PacienteForm, MedicoForm
from django.views.decorators.http import require_POST

def turnos_lista(request):
    turnos = Turno.objects.all()
    return render(request, 'lista.html', {'turnos': turnos})

def detalle_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    return render(request, 'detalle_turno.html', {'turno': turno})

def aniadir_turno(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST, prefix='paciente')
        medico_form = MedicoForm(request.POST, prefix='medico')
        turno_form = TurnosForm(request.POST, prefix='turno')

        if paciente_form.is_valid() and medico_form.is_valid() and turno_form.is_valid():
            # Crear o recuperar paciente/medico
            paciente_data = paciente_form.cleaned_data
            paciente, _ = Paciente.objects.update_or_create(
                dni=paciente_data['dni'],
                defaults={
                    'nombre': paciente_data['nombre'],
                    'fecha_nac': paciente_data['fecha_nac'],
                    'contacto': paciente_data['contacto'],
                },
            )

            medico_data = medico_form.cleaned_data
            medico, _ = Medico.objects.update_or_create(
                num_matricula=medico_data['num_matricula'],
                defaults={
                    'nombre': medico_data['nombre'],
                    'dni': medico_data['dni'],
                    'contacto': medico_data['contacto'],
                },
            )

            # Validación de duplicado (misma fecha, hora y médico)
            fecha = turno_form.cleaned_data['fecha']
            hora = turno_form.cleaned_data['hora']
            if Turno.objects.filter(fecha=fecha, hora=hora, medico=medico).exists():
                turno_form.add_error(None, 'Ya existe un turno para este médico en esa fecha y hora.')
            else:
                turno = turno_form.save(commit=False)
                turno.paciente = paciente
                turno.medico = medico
                turno.save()
                return redirect('lista')
    else:
        paciente_form = PacienteForm(prefix='paciente')
        medico_form = MedicoForm(prefix='medico')
        turno_form = TurnosForm(prefix='turno')

    return render(request, 'aniadir_turno.html', {
        'paciente_form': paciente_form,
        'medico_form': medico_form,
        'turno_form': turno_form,
    })


@require_POST
def eliminar_turno(request, turno_id):
    turno = get_object_or_404(Turno, id=turno_id)
    turno.delete()
    return redirect('lista')