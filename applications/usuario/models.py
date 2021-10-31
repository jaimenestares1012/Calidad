from django.db import models

class Usuario(models.Model):
     dni_usuario=models.IntegerField('Dni')
     nombres=models.CharField('Nombres', max_length=50)
     apellidos = models.CharField('Apellidos', max_length=50)
     nro_departamento=models.IntegerField('N° departamento')
     correo=models.EmailField('Correo')
     celular=models.IntegerField('Celular')
     class meta:
         verbose_name='Usuario'
         verbose_name_plural='Usuarios'
     def __str__(self):
         return self.nombres + ' ' + self.apellidos 
