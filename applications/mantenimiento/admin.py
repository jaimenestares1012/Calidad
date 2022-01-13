from django.contrib import admin
from .models import Externos, trabajo_mantenimiento
# Register your models here.

# se registra el mdoelo al admins
class TrabajoMantenimientoAdmin(admin.ModelAdmin):
    # se crea el list display en 
    list_display=(
        'id',
        'nro_trabajadores',
        'dia_mantenimiento',
        'hora_mantenimiento',
    )
     # se crea un metoo de busque para el admin
    search_fields=('dia_mantenimiento',)


# se registra el mdoelo al adminstradores
class ExternoAdmin(admin.ModelAdmin):
    list_display=(
        'dni_externo',
        'nombre_externo',
        'apellido_externo',
        'trabajo_mantenimientos',
    )
    # se crea un metoo de busque para el admintradosres
    search_fields=('nombre_mantenimiento',)

# se hace las vinculaciones de trabajo y los externos
admin.site.register(trabajo_mantenimiento, TrabajoMantenimientoAdmin)
admin.site.register(Externos, ExternoAdmin)