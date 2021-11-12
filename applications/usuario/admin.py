from django.contrib import admin
from .models import  Usuario
# Register your models here.




class UsuarioAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'nro_departamento',
        'dni_usuario',
        'nombres',
        'apellidos',
        'celular'
    )

    def full_name(self, obj):
        return obj.first_name +' '+ obj.last_name 
    search_fields=('nombres',)

admin.site.register(Usuario, UsuarioAdmin)
