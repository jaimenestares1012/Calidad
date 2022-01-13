from django.views.generic import TemplateView
from django.urls import reverse_lazy
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    # template de prueba
    template_name='administracion/index.html'


# creamos el view de inicio de sesion
class InicioSesion(LoginRequiredMixin, TemplateView):
    # usamo el panel.html como web
    template_name = 'administracion/panel.html'
    login_url = reverse_lazy('users:iniciar-sesion')

class FechaMixin(object):
    # creamos la fecha mixin para validar
    def get_context_data(self, **kwargs):
        # mandmos por defecto a un context
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context






