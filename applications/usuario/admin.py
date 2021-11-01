from django.contrib import admin
from .models import Pago, Usuario
# Register your models here.

class UsuarioPagoInline(admin.TabularInline):
    model = Pago
    extra = 1


class UsuarioAdmin(admin.ModelAdmin):
    inlines = (UsuarioPagoInline,)
    list_display=(
        'id',
        'nro_departamento',
        'dni_usuario',
        'nombres',
        'apellidos',
        'correo',
        'celular'
    )

    def full_name(self, obj):
        return obj.first_name +' '+ obj.last_name 
    search_fields=('nombres',)

admin.site.register(Usuario, UsuarioAdmin)
