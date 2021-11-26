import datetime
from datetime import timedelta 
from applications.actividades.models import Actividades
class PruebaMiddleware:
    def __init__(self, get_response) :
        self.get_response=get_response

    def __call__(self, request) :
        
        response=self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            fecha_actual= datetime.date.today()
            reservas=Actividades.objects.filter(estado="Pendiente")
            for reserva in reservas:
                fecha_vencimiento = reserva.fecha_reserva + timedelta(days=1)
                if fecha_actual>fecha_vencimiento:
                    reserva.estado="no pendiente"
                    reserva.save()
       

