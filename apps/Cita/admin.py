from django.contrib import admin
from .models import Cita,Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'medico', 'servicio', 'fecha_hora', 'estado')
    search_fields = ('cliente__nombre', 'medico__nombre', 'servicio__nombre')
# Register your models here.
