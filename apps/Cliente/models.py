from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    apellido = models.CharField(max_length=100,blank=False, null=False)
    email = models.EmailField(blank=False, null=False,help_text="Ingrese su correo electrónico ",unique=True)
    telefono = models.CharField(max_length=20,blank=False, null=False)
    direccion = models.CharField(max_length=200,blank=False, null=False)

    class tipo_documento(models.TextChoices):
        Tarjeta_Identidad = 'TI', 'Tarjeta de Identidad'
        cedula = 'CC', 'Cédula de Ciudadanía'
        pasaporte = 'PASSPORT', 'Pasaporte'
        otro = 'OTRO', 'Otro'
    tipo_documento = models.CharField(max_length=20, choices=tipo_documento.choices, default=tipo_documento.otro)
    numero_documento = models.CharField(max_length=50,blank=False, null=False,unique=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class meta:
        db_table = 'Tabla_de_clientes'
        verbose_name_plural = 'Clientes'

