from django import forms
import datetime

from django.forms import widgets
from .models import Actividades


class DateInput(forms.DateInput):
    input_type = 'date'


class my_actividades_form(forms.ModelForm):


    class Meta:

        model = Actividades
        fields = (
            'fecha_reserva',
            'hora_reserva',
            'espacio',
        )
        widgets = {
            'fecha_reserva': DateInput
        }

    def clean_fecha_reserva(self):

        fecha_actual = datetime.date.today()
        
        fecha_reserva = self.cleaned_data['fecha_reserva']
        print("esta es la fecha de reserva en el forms", fecha_reserva)
        print(type(fecha_reserva))
        fecha1 = datetime.date(2023, 1, 1)
        if fecha_reserva>fecha1:
            raise forms.ValidationError(
                "ingrese una fecha más proxima, fecha máxima: 2023-01-01")
        print(type(fecha1))
        # fecha_reserva=fecha_reserva.split("-")
        print("wdeidiededede",fecha_reserva)
        if fecha_reserva < fecha_actual:
            raise forms.ValidationError(
                "ingrese una fecha correcta de su reserva ")

        
        return fecha_reserva

