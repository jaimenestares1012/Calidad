import datetime
from datetime import timedelta 
from applications.servicio.models import Servicio
class MidServicios:
    def __init__(self, get_response) :
        self.get_response=get_response

    def __call__(self, request) :
        
        response=self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            fecha_actual= datetime.date.today()
            reservas=Servicio.objects.filter(estado="Pagado")
            print(reservas, fecha_actual , "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")

            
            for reserva in reservas:
                reserva.fecha_cancelacion=fecha_actual
                reserva.save()
       

