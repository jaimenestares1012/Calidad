from django.db import models
from applications.materiales.models import Material
class Trabajador(models.Model):
     funciones = (
        ('1', 'Personal limpieza'),
        ('2', 'Vigilante'),
        ('3', 'Conserje'),
        ('4', 'Recepcionista'),

     )
     dni_empledo= models.IntegerField('Dni')
     nombre_empleado= models.CharField('Nombre', max_length=50)
     apellidos_empleado=models.CharField('Apellidos', max_length=50)
     funcion= models.CharField('Funcion',max_length=50 ,choices=funciones)
     
     class meta:
         verbose_name='Trabajador'
         verbose_name_plural='Trabajadores'
     def __str__(self):
         return  self.nombre_empleado 


class Trabajo(models.Model):
        trabajador=models.ForeignKey(Trabajador, on_delete=models.CASCADE)
        fecha=models.DateField("Fecha")
        materiales=models.ForeignKey(Material, on_delete=models.CASCADE )
        class meta:
            verbose_name = 'Trabajo'
            verbose_name_plural = 'Trabajos'

        def __str__(self):
            return str(self.id) + '-' + str(self.trabajador) + '-' + str(self.fecha) + '-'  + str(self.materiales)