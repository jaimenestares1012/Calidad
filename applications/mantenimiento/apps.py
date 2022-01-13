from django.apps import AppConfig

# se añade debido a django 3.0
class MantenimientoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.mantenimiento'
