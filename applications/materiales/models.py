from django.db import models

# Create your models here.
class Material(models.Model):
    nombre = models.CharField('Material', max_length=50)
    precio = models.IntegerField('Precio')
    stock_actual = models.IntegerField('Stock')

    class meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales disponibles'

    def __str__(self):
        return  self.nombre