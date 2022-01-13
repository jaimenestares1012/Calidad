from django.db import models
from applications.usuario.models import Usuario
# Create your models here.
class trabajo_mantenimiento(models.Model):
    # se crea el arreglo de horas
    horas = (
        ('5', '05 am'),
        ('6', '06 am'),
        ('7', '07 am'),
        ('8', '08 am'),
        ('9', '09 am'),
        ('10', '10 am'),
        ('11', '11 am'),
        ('12', '12 pm'),
        ('13', '01 pm'),
        ('14', '02 pm'),
        ('15', '03 pm'),
        ('16', '04 pm'),
        ('17', '05 pm'),
        ('18', '06 pm'),
        ('19', '07 pm'),
        ('20', '08 pm'),
        ('21', '09 pm'),
        ('22', '10 pm'),
        ('23', '11 pm'),
        ('24', '12 am'),
        ('1', '01 am'),
        ('2', '02 am'),
        ('3', '03 am'),
        ('4', '04 am'),
    )
    # se crea las demas variable
    nro_trabajadores=models.IntegerField("N° trabajadores")
    dia_mantenimiento=models.DateField("Fecha")
    hora_mantenimiento=models.CharField("Hora", max_length=12 ,choices=horas)
    descripcion=models.CharField("Descripción", max_length=60, blank=True)
    nro_departamento=models.IntegerField("nro departamento", blank=True )
    usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE)
    

    # creamos la clase meta
    class Meta:
        # en singular
        verbose_name = 'Mantenimiento'
        # en singular
        verbose_name_plural = "Trabajos de mantenimientos"
        # lo ordemos por el dia de mantenimiento
        ordering = ['dia_mantenimiento']
    # se define la estructura de como se mostrara
    def __str__(self):
        # se retona solo una descrirpcion
        return self.descripcion

# se crea la clase externos
class Externos(models.Model):
    dni_externo = models.IntegerField("Dni externo")
    nombre_externo = models.CharField("nombre", max_length=50)
    apellido_externo = models.CharField("apellido", max_length=50)
    trabajo_mantenimientos = models.ForeignKey(trabajo_mantenimiento, on_delete=models.CASCADE)
    # creamos la clase meta de externos
    class Meta:
        # en singular de externos
        verbose_name = 'Externos'
        # en plural de extwenos
        verbose_name_plural = "Trabajadores externos"
    # se define la estuctura de como se mostra
    def __str__(self):
        # se retorna solo el id
        return str(self.id)

