from django.db import models

# Create your models here.

# dinimos el tipo de adminsitrador
class Administrador(models.Model):
    tipo_administrador = models.CharField("tipo", max_length=50)
    # desaroolamos el meta 
    class meta:
        # en plural
        verbose_name = 'Aministrador'
        # en plurasles
        verbose_name_plural = 'Administradores'
    # definismo el str
    def __str__(self):
        # retonamos dos variables
        return str(self.id) + '-' + self.tipo_administrador