from django.contrib import admin
from .models import Actividades
# Register your models here.



# Registramos a las activdades en el admin
class ActividadesAdmin(admin.ModelAdmin):
    #selecciionamos las variables a obersvar
    list_display=(
        'id',
        'fecha_reserva',
        'hora_reserva',
        'espacio',
        'estado',
        'usuario',
    )
    # estos son los filtos qque se usan
    list_filter=('espacio',)
    # Este es la opcion de busqueda d
    search_fields=('usuario',)
# registradfo y vinculado
admin.site.register(Actividades, ActividadesAdmin)