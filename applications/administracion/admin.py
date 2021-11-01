from django.contrib import admin
from .models import Administrador
# Register your models here.




class AdministradorAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'tipo_administrador',
    )


admin.site.register(Administrador, AdministradorAdmin)