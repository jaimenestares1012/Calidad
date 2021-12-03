from django.views.generic import TemplateView, ListView, CreateView
from applications.visita.models import Visita, Visitantes
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .forms import visitaForm, visitantesForm
# Create your views here.
class prueba(ListView):
    template_name='visita/prueba.html'
    model=Visita


    def get_queryset(self):
        lista = Visita.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pendiente"
        )
        return lista

class visitaCreateView(LoginRequiredMixin,CreateView):
    model =Visita
    template_name = "visita/add_visita.html"
    login_url = reverse_lazy('users:user-login')
    form_class= visitaForm
    success_url = reverse_lazy('visita:lista_visita')


class visitantesCreateView(LoginRequiredMixin, CreateView):
    model = Visitantes
    template_name = "visita/add_visitantes.html"
    login_url = reverse_lazy('users:user-login')
    form_class = visitantesForm
    success_url = reverse_lazy('actividades:success')

