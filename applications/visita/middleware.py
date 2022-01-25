import datetime
from datetime import timedelta
from applications.visita.models import Visita

# se hace la creacion de los midd
class PruebaMiddlewareVisita:
    # se inicializa la funcion
    def __init__(self, get_response):
        self.get_response = get_response
    # se llama la funcion
    def __call__(self, request):
        # se tiene un response
        response = self.get_response(request)
        return response
    # se crea un porcess view
    def process_view(self, request, view_func, view_args, view_kwargs):
        # se crea la decision
        if request.user.is_authenticated:
            # se fecha actuañ
            fecha_actual = datetime.date.today()
            # se determina la reserva
            reservas = Visita.objects.filter(estado="Pendiente")
            # se crea un iterable de reservas
            for reserva in reservas:
                # se captura fecha de vencimiento
                fecha_vencimiento = reserva.fecha_visita + timedelta(days=0)
                # se hace la decicion
                if fecha_actual > fecha_vencimiento:
                    # se reserva el estado en no penditente
                    reserva.estado = "no pendiente"
                    # se hace el guaradado
                    reserva.save()
