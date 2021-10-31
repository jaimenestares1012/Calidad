from django.db import models

# Create your models here.
class Trabajo_mantenimiento(models.Model):
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
    nro_trabajadores=models.IntegerField("N° trabajadores")
    dia_mantenimiento=models.DateTimeField("Fecha")
    hora_mantenimiento=models.IntegerField("Hora", choices=horas)


    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = "Trabajos de mantenimientos"
        ordering = ['dia_mantenimiento']

    def __str__(self):
        return str(self.id) + '-' + self.dia_mantenimiento + '-' + self.hora_mantenimiento


class Externos(models.Model):
    dni_externo = models.IntegerField("Dni externo")
    nombre_externo = models.CharField("nombre", max_length=50)
    apellido_externo = models.CharField("apellido", max_length=50)
    trabajo_mantenimiento = models.ForeignKey(Trabajo_mantenimiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Externos'
        verbose_name_plural = "Trabajadores externos"

    def __str__(self):
        return str(self.id) + '-' + self.nombre_externo + '-' + self.apellido_externo + '-' + self.trabajo_mantenimiento

