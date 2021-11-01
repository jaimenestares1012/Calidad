from django.db import models

from applications.usuario.models import Usuario


class Actividades(models.Model):
     Espacio = (
        ('1', 'Piscina'),
        ('2', 'Área parrilla'),
        ('3', 'Sala star'),
        ('4', 'Área recreativa'),

     )
     fecha_reserva = models.DateField("fecha reserva")
     espacio=models.CharField("Espacio", max_length=20, choices=Espacio)
     usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE)

     class meta:
         verbose_name='Actividad'
         verbose_name_plural='Actividades'
     def __str__(self):
         return   str(self.espacio) +'-' + str(self.usuario)
