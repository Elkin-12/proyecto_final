from django.db import models
from apps.Cliente.models import Cliente
from apps.Medico.models import Medico
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'Tabla_de_servicios'
        verbose_name_plural = 'Servicios'

class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    class estado_cita(models.TextChoices):
        pendiente = 'PENDIENTE', 'Pendiente'
        confirmada = 'CONFIRMADA', 'Confirmada'
        cancelada = 'CANCELADA', 'Cancelada'
    estado = models.CharField(max_length=20, choices=estado_cita.choices, default=estado_cita.pendiente)
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT, related_name='citas')
    medico = models.ForeignKey(Medico,on_delete=models.PROTECT, related_name='citas')
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT, related_name='citas')
    def __str__(self):
        fecha_formateada = self.fecha_hora.strftime('%d/%m/%Y %H:%M')
        return f"Cita [{fecha_formateada}] - {self.servicio.nombre} | Paciente: {self.cliente} | Dr(a). {self.medico.apellido}"
    class Meta:
        db_table = 'Tabla_de_citas'
        verbose_name_plural = 'Citas'


