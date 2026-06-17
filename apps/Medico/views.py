from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Medico, Especialidad


def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'Medico/lista_medicos.html', {'medicos': medicos})


def registrar_medico(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        especialidades_ids = request.POST.getlist('especialidad') 
        
        nuevo_medico = Medico.objects.create(nombre=nombre, apellido=apellido)
        nuevo_medico.especialidad.set(especialidades_ids) # Asigna las relaciones ManyToMany
        
        return redirect('lista_medicos') 

    especialidades = Especialidad.objects.all()
    return render(request, 'Medico/registro_medico.html', {'especialidades': especialidades})

def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'Medico/lista_especialidades.html', {'especialidades': especialidades})

def registrar_especialidad(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Especialidad.objects.create(nombre=nombre)
    return redirect('lista_especialidades')

def eliminar_medico(request, medico_id):
    if request.method == 'POST':
        medico = get_object_or_404(Medico, id=medico_id)
        try:
            nombre_completo = f"Dr(a). {medico.nombre} {medico.apellido}"
            medico.delete()
            messages.success(request, f"Médico '{nombre_completo}' eliminado correctamente.")
        except ProtectedError:
            messages.error(request, f"No se puede eliminar al médico 'Dr(a). {medico.nombre} {medico.apellido}' porque tiene citas médicas asignadas en el sistema.")
    return redirect('lista_medicos')