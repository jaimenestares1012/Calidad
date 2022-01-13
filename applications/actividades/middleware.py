import datetime
from datetime import timedelta 
from applications.actividades.models import Actividades

# Se crea un middleware para pasar de estados las peticiones
class PruebaMiddleware:
    # se inicioliza la funcion
    def __init__(self, get_response) :
        self.get_response=get_response
    # se crea la funcion call 
    def __call__(self, request) :
        # se hace una prueba
        response=self.get_response(request)

        # se retorna la prueba
        return response


    # se hace el proceso de validacion 
    def process_view(self, request, view_func, view_args, view_kwargs):
        # se define un condicional
        if request.user.is_authenticated:
            # se captura la fehca actuall
            fecha_actual= datetime.date.today()
            # se filtra por los estamos pendientes de las reservas
            reservas=Actividades.objects.filter(estado="Pendiente")
            # se inicia el iterador
            for reserva in reservas:
                #se recorre la lista de objetos
                fecha_vencimiento = reserva.fecha_reserva + timedelta(days=1)
                # se entra al siguiente decuion
                if fecha_actual>fecha_vencimiento:
                    #se hace el cambio de estado
                    reserva.estado="no pendiente"
                    # se hace el guadrado en la bd
                    reserva.save()
       

