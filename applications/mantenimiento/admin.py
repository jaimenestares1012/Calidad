from django.contrib import admin
from .models import Externos, trabajo_mantenimiento
# Register your models here.


class TrabajoMantenimientoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'nro_trabajadores',
        'dia_mantenimiento',
        'hora_mantenimiento',
    )

    search_fields=('dia_mantenimiento',)


class ExternoAdmin(admin.ModelAdmin):
    list_display=(
        'dni_externo',
        'nombre_externo',
        'apellido_externo',
        'trabajo_mantenimientos',
    )

    search_fields=('nombre_mantenimiento',)


admin.site.register(trabajo_mantenimiento, TrabajoMantenimientoAdmin)
admin.site.register(Externos, ExternoAdmin)