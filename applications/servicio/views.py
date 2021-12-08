
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .utils import render_to_pdf
from applications.servicio.models import Servicio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View

# impotamos el modelo para trabjar con ellas en el template

# Create your views here.
variable = 'users:iniciar-sesion'

class prueba(TemplateView):
    template_name = 'servicio/prueba.html'


class ListaServicios(LoginRequiredMixin, ListView):
    template_name = 'servicio/ListaServicios.html'
    login_url = reverse_lazy(variable)

    def get_queryset(self):
        lista = Servicio.objects.filter(
            usuario__users__username=self.request.user,
            estado="Adeudado"
        )
        return lista


class RealizarPago(LoginRequiredMixin, ListView):
    template_name = 'servicio/pasarella.html'
    login_url = reverse_lazy(variable)
    context_object_name = 'pagos'

    def get_queryset(self):
        area = self.kwargs['id']
        lista = Servicio.objects.filter(
            id=area
        )
        return lista


class ListaRecibos(LoginRequiredMixin, ListView):
    template_name = 'servicio/ListaRecibos.html'
    login_url = reverse_lazy(variable)

    def get_queryset(self):

        lista = Servicio.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pagado",

        )
        return lista

class ListPdf2(LoginRequiredMixin,View):
    login_url = reverse_lazy(variable)
    def get(self, request, *args, **kwargs):
        area = self.kwargs['shorname']
        servicio = Servicio.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pagado",
            id=area
        )
        data = {
            'servicios': servicio
        }
        pdf = render_to_pdf('servicio/ListaPdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
