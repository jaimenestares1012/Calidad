from django.contrib import admin
from .models import Material
# Register your models here.


class MaterialAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'nombre',
        'precio',
        'stock_actual',
    )

    search_fields=('nombre',)

admin.site.register(Material, MaterialAdmin)
