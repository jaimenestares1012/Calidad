from django.views.generic import TemplateView, ListView, CreateView

#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    # se determina el template
    template_name='usuario/prueba.html'

