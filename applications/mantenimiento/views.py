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
class prueba(TemplateView):
    template_name='mantenimiento/prueba.html'

class ListaMantenimiento(LoginRequiredMixin, ListView):
    template_name = 'mantenimiento/lista-mantenimiento.html'
    login_url = reverse_lazy("users:iniciar-sesion")
    

    
    def get_queryset(self):
        visi1 = self.kwargs['shorname']
        lista = trabajo_mantenimiento.objects.filter(
            usuario__users__username=self.request.user,
        )
        return lista

class mantenimiento_view(LoginRequiredMixin, FormView):
    model =trabajo_mantenimiento
    template_name = "mantenimiento/add_mantenimiento.html"
    login_url = reverse_lazy("users:iniciar-sesion")
    form_class= my_mantenimiento_form
    success_url = '/mantenimiento/lista-mantenimiento/Usuarios'
    def form_valid(self, form):
        
        id_usuario = self.request.user.id
        usuario = Usuario(
            id=id_usuario,
        )
        
        nro_trabajadores = form.cleaned_data['nro_trabajadores']
        dia_mantenimiento = form.cleaned_data['dia_mantenimiento']
        hora_mantenimiento = form.cleaned_data['hora_mantenimiento']
        descripcion = form.cleaned_data['descripcion']
        nro_departamento = form.cleaned_data['nro_departamento']
        
        
        trabajo_mantenimiento.objects.create(
            nro_trabajadores=nro_trabajadores,
            dia_mantenimiento=dia_mantenimiento,
            hora_mantenimiento=hora_mantenimiento,
            descripcion=descripcion,
            nro_departamento=nro_departamento,
            usuario=usuario
        )
        # print("tener cuidado de un posible error ",id_usuario, self.request.user , fecha_visita, nro_personas)
        
        return super(mantenimiento_view, self).form_valid(form)


class ListaMantenimientosPropias(LoginRequiredMixin, ListView):
    template_name = "mantenimiento/detalle_mantenimiento.html"
    login_url = reverse_lazy("users:iniciar-sesion")

    def get_queryset(self):

        # espacio = self.kwargs['shorname']

        lista = trabajo_mantenimiento.objects.filter(
            usuario__users__username=self.request.user,
        )
        return lista


class Externos_view(LoginRequiredMixin, FormView):
    model = Externos
    template_name = "mantenimiento/add_externos.html"
    login_url = reverse_lazy("users:iniciar-sesion")
    form_class = ExternosForm
    success_url = '/mantenimiento/mis-mantenimientos'

    def form_valid(self, form):
        visi1 = self.kwargs['shorname']
        visi = trabajo_mantenimiento(
            id=visi1,
        )

        dni = form.cleaned_data['dni_externo']
        nombre = form.cleaned_data['nombre_externo']
        apellido = form.cleaned_data['apellido_externo']

        Externos.objects.create(
            dni_externo=dni,
            nombre_externo=nombre,
            apellido_externo=apellido,
            trabajo_mantenimientos=visi
        )
        print("*************************estamos en los forma valid")
        return super(Externos_view, self).form_valid(form)

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