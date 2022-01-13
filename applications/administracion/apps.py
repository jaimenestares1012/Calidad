from django.apps import AppConfig

# el modelo administracion se usa poco por lo qye aun esta en mantienimiento
class AdministracionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.administracion'
