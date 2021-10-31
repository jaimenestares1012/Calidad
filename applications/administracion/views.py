from django.views.generic import TemplateView, ListView, CreateView

#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    template_name='administracion/index.html'

class InicioSesion(TemplateView):
    template_name = 'administracion/iniciar_sesion.html'