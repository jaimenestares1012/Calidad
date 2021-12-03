from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import FormView
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


class visitantesCreateView(LoginRequiredMixin, FormView):
    model = Visitantes
    template_name = "visita/add_visitantes.html"
    login_url = reverse_lazy('users:user-login')
    form_class = visitantesForm
    success_url = reverse_lazy('actividades:success')

    def form_valid(self, form):
        visi1 = self.kwargs['shorname']
        visi=Visita(
            id=visi1,
        )

        dni = form.cleaned_data['dni_visita']
        nombre = form.cleaned_data['nombre_visita']
        apellido = form.cleaned_data['apellido_visita']
        
        Visitantes.objects.create(
            dni_visita=dni,
            nombre_visita=nombre,
            apellido_visita=apellido,
            visita=visi
        )
        print("*************************estamos en los forma valid")
        return super(visitantesCreateView, self).form_valid(form)

