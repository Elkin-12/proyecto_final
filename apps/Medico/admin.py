from django.contrib import admin
from .models import Medico, Especialidad
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad_list')
    def especialidad_list(self, obj):
        return ", ".join([especialidad.nombre for especialidad in obj.especialidad.all()])
    search_fields = ('nombre', 'apellido', 'especialidad__nombre')
# Register your models here.
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',) 