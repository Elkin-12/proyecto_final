from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Medico, Especialidad
from .forms import MedicoForm, EspecialidadForm

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'Medico/lista_medicos.html', {'medicos': medicos})


def registrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Médico registrado correctamente.")
            return redirect('lista_medicos')
    else:
        form = MedicoForm()
    
    return render(request, 'Medico/registro_medico.html', {'form': form})



def registrar_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Especialidad creada con éxito.")
    return redirect('lista_especialidades')

def eliminar_medico(request, medico_id):
    if request.method == 'POST':
        try:
            medico = get_object_or_404(Medico, id=medico_id)
            nombre_completo = f"Dr(a). {medico.nombre} {medico.apellido}"
            medico.delete()
            messages.success(request, f"Médico '{nombre_completo}' eliminado correctamente.")
        except ProtectedError:
            messages.error(request, "No se puede eliminar al médico porque tiene citas médicas asignadas en el sistema.")
            
    return redirect('lista_medicos')

def editar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, f"Médico {medico.nombre} actualizado correctamente.")
            return redirect('lista_medicos')
    else:
        form = MedicoForm(instance=medico)
        
    return render(request, 'Medico/editar_medico.html', {'form': form, 'medico': medico})

def lista_especialidades(request):
    if request.method == 'POST':
        especialidad_id = request.POST.get('especialidad_id')
        if especialidad_id:
            especialidad = get_object_or_404(Especialidad, id=especialidad_id)
            form = EspecialidadForm(request.POST, instance=especialidad)
            if form.is_valid():
                form.save()
                messages.success(request, f"Especialidad '{especialidad.nombre}' actualizada correctamente.")
        else:
            form = EspecialidadForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Especialidad creada con éxito.")
                
        return redirect('lista_especialidades')
    especialidades = Especialidad.objects.all()
    form = EspecialidadForm() 
    
    return render(request, 'Medico/lista_especialidades.html', {
        'especialidades': especialidades, 
        'form': form
    })
def eliminar_especialidad(request, especialidad_id):
    if request.method == 'POST':
        try:
            especialidad = get_object_or_404(Especialidad, id=especialidad_id)
            nombre_esp = especialidad.nombre
            especialidad.delete()
            messages.success(request, f"Especialidad '{nombre_esp}' eliminada correctamente.")
        except ProtectedError:
            messages.error(request, "No se puede eliminar la especialidad porque hay médicos asignados a ella.")
            
    return redirect('lista_especialidades')