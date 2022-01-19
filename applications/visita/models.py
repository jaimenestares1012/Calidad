from django.db import models

from applications.usuario.models import Usuario


class Visita(models.Model):
     fecha_visita = models.DateField("fecha de visita")
     usuario = models.ForeignKey(
         Usuario, on_delete=models.CASCADE)
     nro_personas=models.IntegerField("Nro de personas")
     estado=models.CharField(max_length=30, default="Pendiente", blank=True)

     class meta:
         verbose_name='Visita'
         verbose_name_plural='Visitas'
     def __str__(self):
         return "Usuario" + str(self.usuario) + "," + " visita: " + str(self.id) + " + " + "fecha_visita: " + str(self.fecha_visita) + " nro_personas: " + str(self.nro_personas)


class Visitantes(models.Model):
    dni_visita=models.IntegerField('Dni visitante')
    nombre_visita=models.CharField('Nombre vistante', max_length=50 )
    apellido_visita=models.CharField('Apellido visitante', max_length=50)
    visita=models.ForeignKey(Visita ,on_delete=models.CASCADE)


    class meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        return str(self.id)  + self.nombre_visita + '-' + self.apellido_visita 