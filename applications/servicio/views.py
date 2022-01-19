
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
# se crea una clase de prueba
class prueba(TemplateView):
    # se define el template
    template_name = 'servicio/prueba.html'

# se crea una clase de lista de servicios
class ListaServicios(LoginRequiredMixin, ListView):
    # se enlaza al tempplate
    template_name = 'servicio/ListaServicios.html'
    # se loguea si es que no esta con un inicio de sesion
    login_url = reverse_lazy(variable)

# se define un queryset
    def get_queryset(self):
        # se hace el filtro en una lista de los servicios
        lista = Servicio.objects.filter(
            usuario__users__username=self.request.user,
            estado="Adeudado"
        )
        
            
        # se retorna la lista filtrada    
        return lista

# se crea el view realizar pago
class RealizarPago(LoginRequiredMixin, ListView):
    # se crea el template y se referencia a la carpeta
    template_name = 'servicio/pasarella.html'
    # se redirige si es que no ha iniciado sesion
    login_url = reverse_lazy(variable)
    # se le da un contect objet name
    context_object_name = 'pagos'
    # se define un  queryset
    def get_queryset(self):
        # se filtra por lo que diga el usuario
        area = self.kwargs['id']
        # se hace el filtro de la lista de servicios

        lista = Servicio.objects.filter(
            id=area
        
        )
        # se retorna la lista
        return lista

# se crea una lista de recibos
class ListaRecibos(LoginRequiredMixin, ListView):
    # se crea el template y se hace referencia a  la carpeta
    template_name = 'servicio/ListaRecibos.html'
    # se redirige si no ha iniciado sesion
    login_url = reverse_lazy(variable)

# se define el quueryset
    def get_queryset(self):
        # se hace el filtro de los servicios
        lista = Servicio.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pagado",
        )
        # se crea una variable tamano
        tamano = len(lista)
        # se hace la deciosion
        if tamano==0:
            # se da un valor por defecto si es que igfual a 0

            lista=1
            # sse retorna con el valor 1
            return lista
            
        else:
            # se retorna la lista completa sin modificaciones
            return lista    
        
# veiew del generar pdf
class ListPdf2(LoginRequiredMixin,View):
    # reverse lazy
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
