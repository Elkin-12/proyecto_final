from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cita, Servicio
from apps.Cliente.models import Cliente
from apps.Medico.models import Medico

def lista_citas(request):
    estado_filtro = request.GET.get('estado')
    citas_query = Cita.objects.all().select_related('cliente', 'medico', 'servicio')
    
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
        fecha_hora = request.POST.get('fecha_hora')
        estado = request.POST.get('estado', 'PENDIENTE')
        cliente_id = request.POST.get('cliente')
        medico_id = request.POST.get('medico')
        servicio_id = request.POST.get('servicio')
        
        Cita.objects.create(
            fecha_hora=fecha_hora,
            estado=estado,
            cliente_id=cliente_id,
            medico_id=medico_id,
            servicio_id=servicio_id
        )
        return redirect('lista_citas')
        
    clientes = Cliente.objects.all()
    medicos = Medico.objects.all()
    servicios = Servicio.objects.all()
    estados = Cita.estado_cita.choices
    
    return render(request, 'Cita/registro_cita.html', {
        'clientes': clientes,
        'medicos': medicos,
        'servicios': servicios,
        'estados': estados
    })

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'Cita/lista_servicios.html', {'servicios': servicios})

def registrar_servicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Servicio.objects.create(nombre=nombre)
    return redirect('lista_servicios')

def cambiar_estado_cita(request, cita_id, estado):
    if estado in ['PENDIENTE', 'CONFIRMADA', 'CANCELADA']:
        try:
            cita = Cita.objects.get(id=cita_id)
            cita.estado = estado
            cita.save()
        except Cita.DoesNotExist:
            pass
    return redirect('lista_citas')

def eliminar_cita(request, cita_id):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, id=cita_id)
        fecha_formateada = cita.fecha_hora.strftime('%d/%m/%Y %H:%M')
        paciente = f"{cita.cliente.nombre} {cita.cliente.apellido}"
        cita.delete()
        messages.success(request, f"Cita del paciente '{paciente}' programada para el {fecha_formateada} ha sido eliminada.")
    return redirect('lista_citas')