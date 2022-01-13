from django.contrib import admin
from .models import Administrador
# Register your models here.


# se crea la administeracion en el model y se muestra en el admon

class AdministradorAdmin(admin.ModelAdmin):
    # se creal el display y sus variables a usar
    list_display=(
        'id',
        'tipo_administrador',
    )


# se vinncula la vista y el modelo
admin.site.register(Administrador, AdministradorAdmin)