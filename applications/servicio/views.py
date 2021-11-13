from django.db import models
from django.views.generic import TemplateView, ListView, CreateView

from applications.servicio.models import Servicio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
#################### impotamos el modelo para trabjar con ellas en el template

# Create your views here.
class prueba(TemplateView):
    template_name='servicio/prueba.html'


class ListaServicios(LoginRequiredMixin, ListView):
    template_name='servicio/ListaServicios.html'  
    login_url = reverse_lazy('users:user-login')
    # model= Servicio
    
    def get_queryset(self) :
        lista = Servicio.objects.filter(
            usuario__users__username= self.request.user
        )
        return lista


class RealizarPago(LoginRequiredMixin, ListView):
    template_name='servicio/pasarella.html' 
    login_url = reverse_lazy('users:user-login')
    model= Servicio