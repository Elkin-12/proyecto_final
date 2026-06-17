from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    def __str__(self):
        return self.nombre
    class meta:
        db_table = 'Tabla_de_especialidades'
        verbose_name_plural = 'Especialidades'

class Medico(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    apellido = models.CharField(max_length=100,blank=False, null=False)
    especialidad = models.ManyToManyField(Especialidad, related_name='medicos')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class meta:
        db_table = 'Tabla_de_medicos'
        verbose_name_plural = 'Medicos'

