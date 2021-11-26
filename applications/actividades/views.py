
from django.views.generic import TemplateView, ListView, CreateView
from applications.actividades.models import Actividades
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from applications.usuario.models import Usuario
# Create your views here.
class prueba(TemplateView):
    template_name='actividades/prueba.html'


# class ListaActividades(LoginRequiredMixin, ListView):
#     template_name='actividades/lista_actividades.html' 
#     login_url = reverse_lazy('users:user-login')
#     model= Actividades
       # def get_queryset(self):
        #     filtro=self.kwargs['url']
        #     lista=Actividades.objects.filter(
        #         Actividades__espacio=filtro
        #     )
        #     return lista


class ListaActividades(LoginRequiredMixin, ListView):
    template_name = 'actividades/lista_actividades.html'
    login_url = reverse_lazy('users:user-login')

    def get_queryset(self):
        lista = Actividades.objects.filter(
            estado="Pendiente",

        )
        return lista


class Success(LoginRequiredMixin, TemplateView):
    template_name = "actividades/success.html"
    login_url = reverse_lazy('users:user-login')


class ActividadesCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:user-login')
    model = Actividades
    template_name = "actividades/create_actividades.html"
    fields = ['fecha_reserva', 'hora_reserva', 'espacio', 'usuario']
    success_url = reverse_lazy('actividades:success')
