from django.views.generic import TemplateView, ListView, CreateView
from applications.visita.models import Visita, Visitantes
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .forms import visitaForm
# Create your views here.
class prueba(TemplateView):
    template_name='visita/prueba.html'



class visitaCreateView(LoginRequiredMixin,CreateView):
    model =Visita
    template_name = "visita/add_visita.html"
    login_url = reverse_lazy('users:user-login')
    form_class= visitaForm
    success_url = reverse_lazy('actividades:success')
