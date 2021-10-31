from django.contrib import admin
from .models import Trabajador, Trabajo
# Register your models here.




class TrabajadorAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'dni_empledo',
        'nombre_empleado',
        'apellidos_empleado',
        'funcion',
    )

    list_filter=('funcion',)
    search_fields=('nombre_empleado',)

class TrabajoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'trabajador',
        'fecha',
        'materiales',
    )

    list_filter=('materiales',)
    search_fields=('trabajador',)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
