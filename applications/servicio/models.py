from django.db import models
from applications.usuario.models import Usuario
class Servicio(models.Model):
     servicio = (
        ('Luz', 'Luz'),
        ('Agua', 'Agua'),
        ('Mantenimiento', 'Mantenimiento'),
     )
     estado=(
         ('Pagado', 'Pagado'),
         ('Adeudado', 'Adeudado'),
     )
     meses=(
         ('Enero', 'Enero'),
         ('Febrero', 'Febrero'),
         ('Marzo', 'Marzo'),
         ('Abril', 'Abril'),
         ('Mayo', 'Mayo'),
         ('Junio', 'Junio'),
         ('Julio', 'Julio'),
         ('Agosto', 'Agosto'),
         ('Septiembre', 'Septiembre'),
         ('Octubre', 'Octubre'),
         ('Noviembre', 'Noviembre'),
         ('Diciembre', 'Diciembre'),

     )
     years = (
         ('2021', '2021'),
         ('2022', '2022'),
         ('2023', '2023'),
         ('2024', '2024'),
         ('2025', '2025'),
         ('2026', '2026'),
         ('2027', '2027'),
         ('2028', '2028'),
         ('2029', '2029'),
         ('2030', '2030'),
         ('2031', '2031'),
         ('2032', '2032'),

     )
     servicio=models.CharField("servicios", max_length=20, choices=servicio)
     monto= models.IntegerField('Monto')
     estado = models.CharField("Estado", max_length=20,choices=estado)
     mes = models.CharField("Mes", max_length=20, choices=meses)
     year=models.CharField("Año", max_length=10, choices=years )

     usuario = models.ForeignKey(
         Usuario,
         
         on_delete=models.CASCADE
     )
     
     class meta:  
         verbose_name='Servicio'
         verbose_name_plural='Servicios'
     def __str__(self):
         return  str(self.monto) 



# class Pago(models.Model):
#     servicio = models.ForeignKey(
#         Servicio, 
#         on_delete=models.CASCADE,
#         blank=True, null=True
#     )
#     usuario = models.ForeignKey(
#         Usuario, 
#         on_delete=models.CASCADE,
#         blank=True, null=True
#     )
#     fecha = models.DateField( 'Fecha')
#     class meta:
#         db_table = 'UsuarioPago'
#         verbose_name = 'Pago'
#         verbose_name_plural = 'Pagos'

#     def __str__(self):
#         return str(self.id) 