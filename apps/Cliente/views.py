from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Cliente
from .forms import ClienteForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Cliente/lista_clientes.html', {'clientes': clientes})


def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) #
        if form.is_valid():              
            form.save()                  
            return redirect('lista_clientes')
    else:
        form = ClienteForm() 

    return render(request, 'Cliente/registro_cliente.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    if request.method == 'POST':
        try:
            cliente = get_object_or_404(Cliente, id=cliente_id)
            nombre_completo = f"{cliente.nombre} {cliente.apellido}"
            
            cliente.delete()
            messages.success(request, f"Paciente '{nombre_completo}' eliminado correctamente.")
        except ProtectedError:
            messages.error(request, f"No se puede eliminar al paciente porque tiene citas médicas u otros registros asociados en el sistema.")      
    return redirect('lista_clientes')

def editar_cliente(request, cliente_id):
    
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save() 
            return redirect('lista_clientes')
    else:
       
        form = ClienteForm(instance=cliente)
        
    return render(request, 'Cliente/editar_cliente.html', {'form': form, 'cliente': cliente})