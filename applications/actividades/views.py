
from django.views.generic import TemplateView, ListView, CreateView
from applications.actividades.models import Actividades
from django.views.generic.edit import FormView
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .forms import actividadesForm

from applications.usuario.models import Usuario
# Create your views here.
class prueba(TemplateView):
    template_name='actividades/prueba.html'



class ListaActividades(LoginRequiredMixin, ListView):
    template_name = 'actividades/lista_actividades.html'
    login_url = reverse_lazy('users:user-login')
    
    def get_queryset(self):
        
        espacio=self.kwargs['shorname']
        
        lista = Actividades.objects.filter(
            estado="Pendiente",
            espacio=espacio,
        )
        return lista
class Success(LoginRequiredMixin, TemplateView):
    template_name = "actividades/success.html"
    login_url = reverse_lazy('users:user-login')


class ActividadesCreateView(LoginRequiredMixin, FormView):
    model = Actividades
    template_name = "actividades/create_actividades.html"
    login_url = reverse_lazy('users:user-login')
    form_class = actividadesForm
    success_url = '/actividades/lista-actividades/Sala star'


    def form_valid(self, form):
        visi1 = self.request.user.id
        usuario = Usuario(
            id=visi1,
        )

        fecha_reserva = form.cleaned_data['fecha_reserva']
        hora_reserva = form.cleaned_data['hora_reserva']
        espacio = form.cleaned_data['espacio']
        
        Actividades.objects.create(
            fecha_reserva=fecha_reserva,
            hora_reserva=hora_reserva,
            espacio=espacio,
            usuario=usuario
        )
        print("*************************estamos en los forma valid")
        return super(ActividadesCreateView, self).form_valid(form)


class ListaActividadesPropias(LoginRequiredMixin, ListView):
    template_name = 'actividades/mis_actividades.html'
    login_url = reverse_lazy('users:user-login')

    def get_queryset(self):

        espacio = self.kwargs['shorname']

        lista = Actividades.objects.filter(
            estado="Pendiente",
            espacio=espacio,
            usuario__users__username=self.request.user,
        )
        return lista
