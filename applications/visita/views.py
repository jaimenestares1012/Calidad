from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import FormView
from applications.visita.models import Visita, Visitantes
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.usuario.models import Usuario
from .forms import visita_form, visitantes_form
# Create your views here.

# se crea la variable de reversion
variable='users:iniciar-sesion'

# se crea una clase de prueba
class prueba(LoginRequiredMixin, ListView):
    #se define el template del view
    template_name='visita/prueba.html'
    # se llama la vatiable
    login_url = reverse_lazy(variable)
    # se trabaja con la visita Visita
    model=Visita

    # se defina un queryset
    def get_queryset(self):
        # se hace los filtros de visita
        lista = Visita.objects.filter(
            usuario__users__username=self.request.user,
            estado="Pendiente"
        )
        # se retorna la lista
        return lista

# se crea la clase visita_view
class visita_view(LoginRequiredMixin, FormView):
    # se define un modelo
    model =Visita
    # se define un template
    template_name = "visita/add_visita.html"
    # se invoca la funcion de variable
    login_url = reverse_lazy(variable)
    # se invoa el form clas con el que se esta trabajando
    form_class= visita_form
    # hay un success url
    success_url = reverse_lazy('visita:lista_visita')

    # se define un form valid
    def form_valid(self, form):
        # se determnia al usuario al que pertenece
        id_usuario = self.request.user.id
        # se hace la invocacion del id
        usuario = Usuario(
            id=id_usuario,
        )
        # la visita y sus filtros
        lista = Visita.objects.filter(
            usuario__users__username=self.request.user,)
        # se itera la lista para ver quiernes y que fechas
        for a in lista:
            print(a.nro_personas)
            print(a.fecha_visita)

        # se crea una fecha visita
        fecha_visita = form.cleaned_data['fecha_visita']
        # se crea el nro de personas
        nro_personas = form.cleaned_data['nro_personas']

        # se hace la creacion por parte deñ view
        Visita.objects.create(
            fecha_visita=fecha_visita,
            nro_personas=nro_personas,
            usuario=usuario
        )
        print("tener cuidado de un posible error ",id_usuario, self.request.user , fecha_visita, nro_personas)
        print("*************************estamos en los forma valid***************************")
        return super(visita_view, self).form_valid(form)


# se define un clase visita view
class visitantes_view(LoginRequiredMixin, FormView):
    # definimos el modelo
    model = Visitantes
    # el tamplate a usar
    template_name = "visita/add_visitantes.html"
    # la reversion un reverse_lazy
    login_url = reverse_lazy(variable)
    # el forma class
    form_class = visitantes_form
    # el succes cuando se tiene exito
    success_url = reverse_lazy('visita:lista_visita')

    # se invoca el form valid
    def form_valid(self, form):
        # se trae el url fianal
        visi1 = self.kwargs['shorname']
        visi=Visita(
            id=visi1,
        )
        # se consolidan las variables
        dni = form.cleaned_data['dni_visita']
        nombre = form.cleaned_data['nombre_visita']
        apellido = form.cleaned_data['apellido_visita']
        
        # se hace la creacion del moedlo
        Visitantes.objects.create(
            dni_visita=dni,
            nombre_visita=nombre,
            apellido_visita=apellido,
            visita=visi
        )
        print("*************************estamos en los forma valid")
        return super(visitantes_view, self).form_valid(form)


# se define una clase lista de visitantes
class list_visitantes(LoginRequiredMixin, ListView):
    template_name = 'visita/lista-visitantes.html'
    # se define el modelo
    model = Visitantes
    # la reversion que se tienen
    login_url = reverse_lazy(variable)
    ###alarma de inserguridad, puede tener errores
    def get_queryset(self):
        # se captura el shorname
        visi1 = self.kwargs['shorname']
        # se hace el filtro
        lista = Visitantes.objects.filter(
            visita__usuario__users__username=self.request.user,
            visita=visi1
        )
        # se retorna la lista
        return lista
