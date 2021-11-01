from django.contrib import admin
from .models import Servicio
# from applications.usuario.admin import UsuarioPagoInline
# Register your models here.




class ServicioAdmin(admin.ModelAdmin):
    # inlines = (UsuarioPagoInline,)
    list_display=(
        'id',
        'servicio',
        'monto',
        'mora',
        'monto_total',
    )

    list_filter=('servicio',)
    search_fields=('servicio',)


admin.site.register(Servicio, ServicioAdmin)

