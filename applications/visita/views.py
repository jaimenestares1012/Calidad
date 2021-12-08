from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import FormView
from applications.visita.models import Visita, Visitantes
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.usuario.models import Usuario
from .forms import visitaForm, visitantesForm
# Create your views here.


class prueba(LoginRequiredMixin, ListView):
    template_name='visita/prueba.html'
    login_url = reverse_lazy('users:user-login')
    model=Visita


    def get_queryset(self):
        lista = Visita.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pendiente"
        )
        return lista


class visita_view(LoginRequiredMixin, FormView):
    model =Visita
    template_name = "visita/add_visita.html"
    login_url = reverse_lazy('users:user-login')
    form_class= visitaForm
    success_url = reverse_lazy('visita:lista_visita')

    def form_valid(self, form):
        
        id_usuario = self.request.user.id
        usuario = Usuario(
            id=id_usuario,
        )

        fecha_visita = form.cleaned_data['fecha_visita']
        nro_personas = form.cleaned_data['nro_personas']

        Visita.objects.create(
            fecha_visita=fecha_visita,
            nro_personas=nro_personas,
            usuario=usuario
        )
        print("tener cuidado de un posible error ",id_usuario, self.request.user , fecha_visita, nro_personas)
        print("*************************estamos en los forma valid***************************")
        return super(visita_view, self).form_valid(form)


class visitantes_view(LoginRequiredMixin, FormView):
    model = Visitantes
    template_name = "visita/add_visitantes.html"
    login_url = reverse_lazy('users:user-login')
    form_class = visitantesForm
    success_url = reverse_lazy('visita:lista_visita')

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
        return super(visitantes_view, self).form_valid(form)


class list_visitantes(LoginRequiredMixin, ListView):
    template_name = 'visita/lista-visitantes.html'
    model = Visitantes
    login_url = reverse_lazy('users:user-login')
    ###alarma de inserguridad, puede tener errores
    def get_queryset(self):
        visi1 = self.kwargs['shorname']
        lista = Visitantes.objects.filter(
            visita__usuario__users__username=self.request.user,
            visita=visi1
        )
        return lista
