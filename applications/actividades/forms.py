from django import forms
import datetime

from django.forms import widgets
from .models import Actividades

# creacion de los principales form
class DateInput(forms.DateInput):
    # Input de prueba
    input_type = 'date'

# form de las actividades
class my_actividades_form(forms.ModelForm):
    # este es el meta de la clas
    class Meta:
        # definimo el modelo
        model = Actividades
        # definimos los input a llenarse
        fields = (
            'fecha_reserva',
            'hora_reserva',
            'espacio',
        )
        # definimos como será la entrada de tipo fecha
        widgets = {
            'fecha_reserva': DateInput
        }
    
    # se realiza las validaciones de tipo fecha
    def clean_fecha_reserva(self):
        # seleccioanmos la fecha actual
        fecha_actual = datetime.date.today()
        # la comparamos con la fecha ingresada
        fecha_reserva = self.cleaned_data['fecha_reserva']
        print("esta es la fecha de reserva en el forms", fecha_reserva)
        print(type(fecha_reserva))
        # desconomponemos la fecha 
        fecha1 = datetime.date(2023, 1, 1)
        # se hace las comparaciones
        if fecha_reserva>fecha1:
            # mostramos el mensaje de validacion
            raise forms.ValidationError(
                "ingrese una fecha más proxima, fecha máxima: 2023-01-01")
        print(type(fecha1))
        # fecha_reserva=fecha_reserva.split("-")
        print("wdeidiededede",fecha_reserva)
        # hacemos la segunda validacion, para que se ingrese la correcta
        if fecha_reserva < fecha_actual:
            raise forms.ValidationError(
                "ingrese una fecha correcta de su reserva ")
        # se retorna la fecha que entro
        return fecha_reserva

