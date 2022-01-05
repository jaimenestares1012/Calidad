from django.views.generic import TemplateView, ListView, CreateView
from applications.mantenimiento.models import trabajo_mantenimiento, Externos
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#################### impotamos el modelo para trabjar con ellas en el template
# from .forms import mantenimiento_form
from applications.usuario.models import Usuario
# Create your views here.
class prueba(TemplateView):
    template_name='mantenimiento/prueba.html'

class ListaMantenimiento(LoginRequiredMixin, ListView):
    template_name = 'mantenimiento/lista-mantenimiento.html'
    login_url = reverse_lazy("users:iniciar-sesion")
    
    # def get_queryset(self):
    #     # visi1 = self.kwargs['shorname']
    #     # lista = Visitantes.objects.filter(
    #     #     visita__usuario__users__username=self.request.user,
    #     #     visita=visi1
    #     # )
    #     return trabajo_mantenimiento

# class visita_view(LoginRequiredMixin, FormView):
#     model =trabajo_mantenimiento
#     template_name = "mantenimiento/add_mantenimiento.html"
#     login_url = reverse_lazy("users:iniciar-sesion")
#     form_class= mantenimiento_form
#     success_url = reverse_lazy('visita:lista_visita')

#     def form_valid(self, form):
        
#         id_usuario = self.request.user.id
#         usuario = Usuario(
#             id=id_usuario,
#         )

#         fecha_visita = form.cleaned_data['fecha_visita']
#         nro_personas = form.cleaned_data['nro_personas']

#         Visita.objects.create(
#             fecha_visita=fecha_visita,
#             nro_personas=nro_personas,
#             usuario=usuario
#         )
#         print("tener cuidado de un posible error ",id_usuario, self.request.user , fecha_visita, nro_personas)
#         print("*************************estamos en los forma valid***************************")
#         return super(visita_view, self).form_valid(form)

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