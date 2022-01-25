from django.db import models

from applications.usuario.models import Usuario

# se crea la clase visita
class Visita(models.Model):
    # se crea la fecha visita
     fecha_visita = models.DateField("fecha de visita")
     # se el usario como un forenkey
     usuario = models.ForeignKey(
         Usuario, on_delete=models.CASCADE)
    # se creal el nro de personas 
     nro_personas=models.IntegerField("Nro de personas")
    # el estado que es un char
     estado=models.CharField(max_length=30, default="Pendiente", blank=True)
    # se determina el meta
     class meta:
         verbose_name='Visita'
         verbose_name_plural='Visitas'
    # se define el str que devuelve
     def __str__(self):
         return "Usuario" + str(self.usuario) + "," + " visita: " + str(self.id) + " + " + "fecha_visita: " + str(self.fecha_visita) + " nro_personas: " + str(self.nro_personas)

# se creal la clase visitantes
class Visitantes(models.Model):
    # dni de la visita
    dni_visita=models.IntegerField('Dni visitante')
    # nombre de la visita
    nombre_visita=models.CharField('Nombre vistante', max_length=50 )
    # apellido de la visita
    apellido_visita=models.CharField('Apellido visitante', max_length=50)
    # el foreing de la visita
    visita=models.ForeignKey(Visita ,on_delete=models.CASCADE)

     # se determina el meta   
    class meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
    # se crea el str
    def __str__(self):
        return str(self.id)  + self.nombre_visita + '-' + self.apellido_visita 