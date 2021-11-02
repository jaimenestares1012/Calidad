
from django.views.generic import TemplateView, ListView, CreateView
from applications.actividades.models import Actividades
#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    template_name='actividades/prueba.html'


class ListaActividades(ListView):
    template_name='actividades/lista_actividades.html'  
    model= Actividades