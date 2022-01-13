
from django.views.generic import TemplateView, ListView, CreateView
from applications.actividades.models import Actividades
from django.views.generic.edit import FormView
#################### impotamos el modelo para trabjar con ellas en el template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .forms import my_actividades_form

from applications.usuario.models import Usuario
# Create your views here.
variable = 'users:iniciar-sesion'
class prueba(TemplateView):
    template_name='actividades/prueba.html'


#lisya de las actividesde que se tienen
class ListaActividades(LoginRequiredMixin, ListView):
    #el tamplate name se guarda en la carpeta actividades
    template_name = 'actividades/lista_actividades.html'
    login_url = reverse_lazy(variable)
    
    #definimos un queryset
    def get_queryset(self):
        #el shorname que viene como parametro, es captdado por la self.kwargs
        espacio=self.kwargs['shorname']
        
        #la lista de actividades, se filtra por, su estado, y lo que viene como tipo, por parte del front
        lista = Actividades.objects.filter(
            estado="Pendiente",
            espacio=espacio,
        )
        return lista


#la clase succes se encarga del mensaje luego de finalizar una acción
class Success(LoginRequiredMixin, TemplateView):

    # se utiliza dicho tamplate
    template_name = "actividades/success.html"
    login_url = reverse_lazy(variable)

# se crea una vista para la creacion de actividades
class ActividadesCreateView(LoginRequiredMixin, FormView):
    # se utiliza el modelo actividades
    model = Actividades
    # usamos el temaplate create-actividades
    template_name = "actividades/create_actividades.html"
    # redireccion si es que no ha iniciado sesion
    login_url = reverse_lazy(variable)
    # se invoca el form utilizado
    form_class = my_actividades_form
    # se crea el succes para cuanod hay exito
    success_url = '/actividades/lista-actividades/Sala star'
    
    # se define el form valid
    def form_valid(self, form):
        # se hace la extraccion del usar
        visi1 = self.request.user.id
        # se invoca al suuario con el paso anterios
        usuario = Usuario(
            id=visi1,
        )
        # se extrae los datos ingresado en el form
        fecha_reserva = form.cleaned_data['fecha_reserva']
        hora_reserva = form.cleaned_data['hora_reserva']
        espacio = form.cleaned_data['espacio']
        print("esta es la fecha de reserva" , fecha_reserva)
        # se crea el objeto actividades y se realiza el filtro total
        Actividades.objects.create(
            fecha_reserva=fecha_reserva,
            hora_reserva=hora_reserva,
            espacio=espacio,
            usuario=usuario
        )
        # se retorna el objt filtrado
        print("*************************estamos en los forma valid")
        return super(ActividadesCreateView, self).form_valid(form)

# se crea un view para la lista de actvidades propias
class ListaActividadesPropias(LoginRequiredMixin, ListView):
    # creamos el template a utilizar
    template_name = 'actividades/mis_actividades.html'
    login_url = reverse_lazy(variable)
    # definimos el get para el filtro
    def get_queryset(self):
        # recepcionamos el espacio que nos pasa por parametro
        espacio = self.kwargs['shorname']
        # se tiene la lista de actividades filtradas
        lista = Actividades.objects.filter(
            estado="Pendiente",
            espacio=espacio,
            usuario__users__username=self.request.user,
        )
        # se retorna la lista con los datos necesarios
        return lista
