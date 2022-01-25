from django.contrib import admin
# se importa la visita y los viistantes
from .models import Visita, Visitantes
# Register your models here.

# se crea el visita
class VisitaAdmin(admin.ModelAdmin):
    # se cerea el viseeta
    list_display=(
        'estado',
        'id',
        'fecha_visita',
        'nro_personas',
        'usuario',
    )
    
    # se hace la busqueda
    search_fields=('fecha_visita',)
# re registra la visita
admin.site.register(Visita, VisitaAdmin)
# re crea el admin
class VisitantesAdmin(admin.ModelAdmin):
    # se crea el display
    list_display=(
        'id',
        'visita',
        'dni_visita',
        'nombre_visita',
        'apellido_visita',

    )
    
    # se creal el filtro
    search_fields=('fecha_visita',)
# se crea el registro en el amdin
admin.site.register(Visitantes, VisitantesAdmin)