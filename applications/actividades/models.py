from django.db import models

from applications.usuario.models import Usuario

# se crea el modelo actividades
class Actividades(models.Model):
     # se crea la lista de espacios
     EspacioLista = (
        ('Piscina', 'Piscina'),
        ('Área parrilla', 'Área parrilla'),
        ('Sala star', 'Sala star'),
        ('Área recreativa', 'Área recreativa'),

     )
     # se crea la lista de horas disponibles
     horas = (
         ('05 am', '05 am'),
         ('06 am', '06 am'),
         ('07 am', '07 am'),
         ('08 am', '08 am'),
         ('09 am', '09 am'),
         ('10 am', '10 am'),
         ('11 am', '11 am'),
         ('12 pm', '12 pm'),
         ('01 pm', '01 pm'),
         ('02 pm', '02 pm'),
         ('03 pm', '03 pm'),
         ('04 pm', '04 pm'),
         ('05 pm', '05 pm'),
         ('06 pm', '06 pm'),
         ('07 pm', '07 pm'),
         ('08 pm', '08 pm'),
         ('09 pm', '09 pm'),
         ('10 pm', '10 pm'),
         ('11 pm', '11 pm'),
         ('12 am', '12 am'),
         ('1 am', '01 am'),
         ('2 am', '02 am'),
         ('3 am', '03 am'),
         ('4 am', '04 am'),
     )
     # se crea la fecha de reserva
     fecha_reserva = models.DateField("fecha reserva" )
     hora_reserva = models.CharField("Hora", max_length=10, choices=horas)
     espacio = models.CharField("Espacio", max_length=20, choices=EspacioLista)
     estado=models.CharField("Estado" , max_length=20, default="Pendiente")
     usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE)
     # se cre la meta del modelo
     class meta:
         # meta singular
         verbose_name='Actividad'
         # meta plural
         verbose_name_plural='Actividades'
     # se crea el metodo str para la devolucion de objtos
     def __str__(self):
         # se retonra los espcio y usuarios
         return   str(self.espacio) +'-' + str(self.usuario)
