from django.views.generic import TemplateView, ListView, CreateView

from applications.servicio.models import Servicio

#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    template_name='servicio/prueba.html'

class ListaServicios(ListView):
    template_name='servicio/ListaServicios.html'  
    model= Servicio