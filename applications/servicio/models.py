from django.db import models

class Servicio(models.Model):
     servicio = (
        ('Luz', 'Luz'),
        ('Agua', 'Agua'),
        ('Mantenimiento', 'Mantenimiento'),
     )
     servicio=models.CharField("servicios", max_length=20, choices=servicio)
     monto= models.IntegerField('Monto')
     mora=models.IntegerField('Mora')
     monto_total=models.IntegerField('Monto total')
     
     class meta:  
         verbose_name='Servicio'
         verbose_name_plural='Servicios'
     def __str__(self):
         return  self.servicio + '-' + str(self.monto) + '-' + str(self.mora) + '-' + str(self.monto_total)



