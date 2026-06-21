from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Cliente/lista_clientes.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        tipo_documento = request.POST.get('tipo_documento')
        numero_documento = request.POST.get('numero_documento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        
        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('lista_clientes')
        
    tipos_doc = Cliente._meta.get_field('tipo_documento').choices
    return render(request, 'Cliente/registro_cliente.html', {'tipos_doc': tipos_doc})

def eliminar_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        try:
            nombre_completo = f"{cliente.nombre} {cliente.apellido}"
            cliente.delete()
            messages.success(request, f"Paciente '{nombre_completo}' eliminado correctamente.")
        except ProtectedError:
            messages.error(request, f"No se puede eliminar al paciente '{cliente.nombre} {cliente.apellido}' porque tiene citas médicas registradas en el sistema.")
    return redirect('lista_clientes')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.tipo_documento = request.POST.get('tipo_documento')
        cliente.numero_documento = request.POST.get('numero_documento')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('lista_clientes')
    
    tipos_doc = Cliente._meta.get_field('tipo_documento').choices
    return render(request, 'Cliente/editar_cliente.html', {'cliente': cliente, 'tipos_doc': tipos_doc})