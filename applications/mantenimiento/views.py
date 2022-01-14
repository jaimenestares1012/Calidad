from django.db import models
from django.views.generic import TemplateView, ListView, CreateView
from applications.mantenimiento.models import trabajo_mantenimiento, Externos
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
#################### impotamos el modelo para trabjar con ellas en el template
from .forms import my_mantenimiento_form, ExternosForm
from applications.usuario.models import Usuario
# Create your views here.
variable = 'users:iniciar-sesion'
class prueba(TemplateView):
    template_name='mantenimiento/prueba.html'
#creacion del view lista de manterniemitnos
class ListaMantenimiento(LoginRequiredMixin, ListView):
    # usamos nuestro template ya creado
    template_name = 'mantenimiento/lista-mantenimiento.html'
    # redirigimos si es que se inicio sesion bien
    login_url = reverse_lazy(variable)
    

    # creamos el quieryset debido a que solo se muestra a usuarios logueados
    def get_queryset(self):
        # tenemos el queryrset del modelo
        visi1 = self.kwargs['shorname']
        # hacemos el filtro
        lista = trabajo_mantenimiento.objects.filter(
            usuario__users__username=self.request.user,
        )
        # se guarda el tamano de la lista filtrada
        tamano = len(lista)
        # se es igual a 0 se retona un numero en su lugar
        if tamano == 0:
            lista = 1
            # retornamos un valor para que se muestre el mensaje de alerta
            return lista
        else:
            return lista
        # retoramos la lista con el firltro de usuarios

class mantenimiento_view(LoginRequiredMixin, FormView):
    # se crea el modelo de trabajo mantenieminto
    model =trabajo_mantenimiento
    # seleccionamos el template
    template_name = "mantenimiento/add_mantenimiento.html"
    # se redirige la pagina
    login_url = reverse_lazy(variable)
    # se selecciona el form creado
    form_class= my_mantenimiento_form

    success_url = '/mantenimiento/lista-mantenimiento/Usuarios'
    #se define un froma valid para la validacion de entrada
    def form_valid(self, form):
        # se extrae el id del usuario con inicio de sesion abierto
        id_usuario = self.request.user.id
        # se saca el id del usuario
        usuario = Usuario(
            id=id_usuario,
        )
        # se invoca los datos de los inputs
        nro_trabajadores = form.cleaned_data['nro_trabajadores']
        dia_mantenimiento = form.cleaned_data['dia_mantenimiento']
        hora_mantenimiento = form.cleaned_data['hora_mantenimiento']
        descripcion = form.cleaned_data['descripcion']
        nro_departamento = form.cleaned_data['nro_departamento']
        
        # se crea el isiaiio mendiante objects
        trabajo_mantenimiento.objects.create(
            nro_trabajadores=nro_trabajadores,
            dia_mantenimiento=dia_mantenimiento,
            hora_mantenimiento=hora_mantenimiento,
            descripcion=descripcion,
            nro_departamento=nro_departamento,
            usuario=usuario
        )
        # print("tener cuidado de un posible error ",id_usuario, self.request.user , fecha_visita, nro_personas)
        # se retona el un super esa lista creada
        return super(mantenimiento_view, self).form_valid(form)

# se crea la vista para manteniemintos propios
class ListaMantenimientosPropias(LoginRequiredMixin, ListView):
    # usmos nuestro template
    template_name = "mantenimiento/detalle_mantenimiento.html"
    login_url = reverse_lazy(variable)
    # definismo un quiery set para los filtros
    def get_queryset(self):

        # espacio = self.kwargs['shorname']

        lista = trabajo_mantenimiento.objects.filter(
            usuario__users__username=self.request.user,
        )
        # se guarda el tamano de la lista filtrada
        tamano = len(lista)
        # se es igual a 0 se retona un numero en su lugar
        if tamano == 0:
            lista = 1
            # retornamos un valor para que se muestre el mensaje de alerta
            return lista
        else:
            return lista
        # retoramos la lista con el firltro de usuarios
        

#cremos la vista para los externos
class Externos_view(LoginRequiredMixin, FormView):
    # definismo el modelo
    model = Externos
    # definimos nuestro template
    template_name = "mantenimiento/add_externos.html"
    # la redireccion si que no hay un  inicio de sesion
    login_url = reverse_lazy(variable)
    # utirlizacion del form class
    form_class = ExternosForm

    success_url = '/mantenimiento/mis-mantenimientos'
    # definimos el form valid
    def form_valid(self, form):
        visi1 = self.kwargs['shorname']
        visi = trabajo_mantenimiento(
            id=visi1,
        )
        # extraemos los datos ingresados por el usuario
        dni = form.cleaned_data['dni_externo']
        nombre = form.cleaned_data['nombre_externo']
        apellido = form.cleaned_data['apellido_externo']
        # creamos un obejts para ingresarlos a la base de datos
        Externos.objects.create(
            dni_externo=dni,
            nombre_externo=nombre,
            apellido_externo=apellido,
            trabajo_mantenimientos=visi
        )
        # retornamos el objeto creado
        print("*************************estamos en los forma valid")
        return super(Externos_view, self).form_valid(form)

# se define un view para la lista de externos
class list_externos(LoginRequiredMixin, ListView):
    template_name = "mantenimiento/list_externos.html"
    # DEFINIMOS UN MODELO PARA LOS EXTERNOS
    model = Externos
    login_url = reverse_lazy(variable)
    # alarma de inserguridad, puede tener errores
    def get_queryset(self):
        visi1 = self.kwargs['shorname']
        lista = Externos.objects.filter(
            trabajo_mantenimientos__usuario__users__username=self.request.user,
            trabajo_mantenimientos=visi1
        )
        # guarfamos el valor de lista, tamaño
        tamano = len(lista)
        # se es igual a 00 se retona un numero en su lugar
        if tamano == 0:
            lista = 1
            # retornamos un vador para que se muestre el mensaje de alerta
            return lista
        else:
            return lista
        



class prueba(ListView):
    print("prueba")
# class visitantes_view(LoginRequiredMixin, FormView):
#     model = Visitantes
#     template_name = "visita/add_visitantes.html"
#     login_url = reverse_lazy(variable)
#     form_class = visitantes_form
#     success_url = reverse_lazy('visita:lista_visita')

#     def form_valid(self, form):
#         visi1 = self.kwargs['shorname']
#         visi=Visita(
#             id=visi1,
#         )

#         dni = form.cleaned_data['dni_visita']
#         nombre = form.cleaned_data['nombre_visita']
#         apellido = form.cleaned_data['apellido_visita']
        
#         Visitantes.objects.create(
#             dni_visita=dni,
#             nombre_visita=nombre,
#             apellido_visita=apellido,
#             visita=visi
#         )
#         print("*************************estamos en los forma valid")
#         return super(visitantes_view, self).form_valid(form)


# class list_visitantes(LoginRequiredMixin, ListView):
#     template_name = 'visita/lista-visitantes.html'
#     model = Visitantes
#     login_url = reverse_lazy(variable)
#     ###alarma de inserguridad, puede tener errores
#     def get_queryset(self):
#         visi1 = self.kwargs['shorname']
#         lista = Visitantes.objects.filter(
#             visita__usuario__users__username=self.request.user,
#             visita=visi1
#         )