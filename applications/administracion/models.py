from django.db import models

# Create your models here.
class Administrador(models.Model):
    tipo_administrador = models.CharField("tipo", max_length=50)

    class meta:
        verbose_name = 'Aministrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return str(self.id) + '-' + self.tipo_administrador