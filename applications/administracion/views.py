from django.views.generic import TemplateView
from django.urls import reverse_lazy
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin

#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    template_name='administracion/index.html'


class InicioSesion(LoginRequiredMixin, TemplateView):
    template_name = 'administracion/panel.html'
    login_url = reverse_lazy('users:user-login')

class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context






