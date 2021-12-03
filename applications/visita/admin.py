from django.contrib import admin
from .models import Visita, Visitantes
# Register your models here.


class VisitaAdmin(admin.ModelAdmin):
    list_display=(
        'estado',
        'id',
        'fecha_visita',
        'nro_personas',
        'usuario',
    )
    
    
    search_fields=('fecha_visita',)

admin.site.register(Visita, VisitaAdmin)

class VisitantesAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'visita',
        'dni_visita',
        'nombre_visita',
        'apellido_visita',

    )
    
    
    search_fields=('fecha_visita',)

admin.site.register(Visitantes, VisitantesAdmin)