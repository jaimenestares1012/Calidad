from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
     
        'id',
        'username'
        
        
        
    )

    search_fields = ('fecha_visita',)


admin.site.register(User, UserAdmin)
