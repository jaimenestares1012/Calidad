from django.contrib import admin
from .models import Actividades
# Register your models here.




class ActividadesAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'fecha_reserva',
        'hora_reserva',
        'espacio',
        'estado',
        'usuario',
    )

    list_filter=('espacio',)
    search_fields=('usuario',)


admin.site.register(Actividades, ActividadesAdmin)