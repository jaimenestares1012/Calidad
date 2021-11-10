
from django.views.generic import TemplateView, ListView, CreateView
from applications.actividades.models import Actividades
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
# Create your views here.
class prueba(TemplateView):
    template_name='actividades/prueba.html'


class ListaActividades(LoginRequiredMixin, ListView):
    template_name='actividades/lista_actividades.html' 
    login_url = reverse_lazy('users:user-login')
    model= Actividades
       # def get_queryset(self):
        #     filtro=self.kwargs['url']
        #     lista=Actividades.objects.filter(
        #         Actividades__espacio=filtro
        #     )
        #     return lista



