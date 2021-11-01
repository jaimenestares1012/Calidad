from django.contrib import admin
from .models import Actividades
# Register your models here.




class ActividadesAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'fecha_reserva',
        'espacio',
        'usuario',
    )

    list_filter=('espacio',)
    search_fields=('usuario',)


admin.site.register(Actividades, ActividadesAdmin)