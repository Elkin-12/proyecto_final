from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cita, Servicio
from .forms import CitaForm, ServicioForm

def lista_citas(request):
    estado_filtro = request.GET.get('estado')
    citas_query = Cita.objects.all().select_related('cliente', 'medico', 'servicio').order_by('-fecha_hora')
   
    total_citas = citas_query.count()
    pendientes = citas_query.filter(estado='PENDIENTE').count()
    confirmadas = citas_query.filter(estado='CONFIRMADA').count()
    canceladas = citas_query.filter(estado='CANCELADA').count()
    
    if estado_filtro in ['PENDIENTE', 'CONFIRMADA', 'CANCELADA']:
        citas = citas_query.filter(estado=estado_filtro)
    else:
        citas = citas_query
        
    return render(request, 'Cita/lista_citas.html', {
        'citas': citas,
        'total_citas': total_citas,
        'pendientes': pendientes,
        'confirmadas': confirmadas,
        'canceladas': canceladas,
        'estado_filtro': estado_filtro
    })

def registrar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita programada correctamente.")
            return redirect('lista_citas')
    else:
        form = CitaForm()
        
    return render(request, 'Cita/registro_cita.html', {'form': form})

def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita actualizada correctamente.")
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
        
    return render(request, 'Cita/editar_cita.html', {'form': form, 'cita': cita})

def cambiar_estado_cita(request, cita_id, estado):
    if request.method == 'POST' and estado in ['PENDIENTE', 'CONFIRMADA', 'CANCELADA']:
        cita = get_object_or_404(Cita, id=cita_id)
        cita.estado = estado
        cita.save()
        messages.success(request, f"Estado de la cita cambiado a {estado}.")
    return redirect('lista_citas')

def eliminar_cita(request, cita_id):
    if request.method == 'POST':
        try:
            cita = get_object_or_404(Cita, id=cita_id)
            fecha_formateada = cita.fecha_hora.strftime('%d/%m/%Y %H:%M')
            paciente = f"{cita.cliente.nombre} {cita.cliente.apellido}"
            cita.delete()
            messages.success(request, f"Cita de '{paciente}' para el {fecha_formateada} eliminada.")
        except Exception:
            messages.error(request, "No se pudo eliminar la cita.")
    return redirect('lista_citas')

def lista_servicios(request):
    if request.method == 'POST':
        servicio_id = request.POST.get('servicio_id')
        if servicio_id:
            
            servicio = get_object_or_404(Servicio, id=servicio_id)
            form = ServicioForm(request.POST, instance=servicio)
            if form.is_valid():
                form.save()
                messages.success(request, "Servicio actualizado correctamente.")
        else:
            form = ServicioForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Servicio creado correctamente.")
        return redirect('lista_servicios')
        
    servicios = Servicio.objects.all()
    form = ServicioForm()
    return render(request, 'Cita/lista_servicios.html', {'servicios': servicios, 'form': form})

def eliminar_servicio(request, servicio_id):
    if request.method == 'POST':
        from django.db.models import ProtectedError
        try:
            servicio = get_object_or_404(Servicio, id=servicio_id)
            servicio.delete()
            messages.success(request, "Servicio eliminado con éxito.")
        except ProtectedError:
            messages.error(request, "No puedes eliminar este servicio porque ya tiene citas registradas.")
    return redirect('lista_servicios')