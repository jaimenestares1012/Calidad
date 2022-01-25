from django.db import models
from applications.users.models import User
# se crea el usuario del user
class Usuario(models.Model):
    # se crea un dni de usuario
     dni_usuario=models.IntegerField('Dni')
       # se crea un nomrbe de usuario
     nombres=models.CharField('Nombres', max_length=50)
       # se crea un apellido de usuario
     apellidos = models.CharField('Apellidos', max_length=50)
       # se crea un nro de departamento de usuario
     nro_departamento=models.IntegerField('N° departamento' , unique=True)
  # se crea un celular de usuario
     celular=models.IntegerField('Celular')
       # se crea un user determinado del usu de usuario
     users = models.ForeignKey(User,  on_delete=models.CASCADE )
  # se el meta a teenr
     class meta:
         verbose_name='Usuario'
         verbose_name_plural='Usuarios'
           # se determina el str, que se devuelve como obj
     def __str__(self):
         return self.nombres + ' ' + self.apellidos 


