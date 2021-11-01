from django.db import models

class Servicio(models.Model):
     servicio = (
        ('1', 'Luz'),
        ('2', 'Agua'),
        ('3', 'Mantenimiento'),
     )
     servicio=models.CharField("servicios", max_length=1, choices=servicio)
     monto= models.IntegerField('Monto')
     mora=models.IntegerField('Mora')
     monto_total=models.IntegerField('Monto total')
     
     class meta:
         verbose_name='Servicio'
         verbose_name_plural='Servicios'
     def __str__(self):
         return  self.nombre_empleado 



