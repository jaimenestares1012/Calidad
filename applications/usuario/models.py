from django.db import models
from applications.servicio.models import  Servicio
class Usuario(models.Model):
     dni_usuario=models.IntegerField('Dni')
     nombres=models.CharField('Nombres', max_length=50)
     apellidos = models.CharField('Apellidos', max_length=50)
     nro_departamento=models.IntegerField('N° departamento')
     correo=models.EmailField('Correo')
     celular=models.IntegerField('Celular')
     servicio = models.ManyToManyField(
        Servicio,
        through='Pago',
        blank=True,
    )

     class meta:
         verbose_name='Usuario'
         verbose_name_plural='Usuarios'
     def __str__(self):
         return self.nombres + ' ' + self.apellidos 


class Pago(models.Model):
    servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    fecha = models.DateField( 'Fecha')
    class meta:
        db_table = 'UsuarioPago'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return str(self.id) + '-' + self.servicio + '-' + self.usuario