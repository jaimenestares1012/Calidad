from django import forms
import datetime

from django.forms import widgets
from .models import Actividades


class DateInput(forms.DateInput):
    input_type = 'date'


class ACTIVIDADES_FORM(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""

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
        if fecha_reserva < fecha_actual:
            raise forms.ValidationError(
                "ingrese una fecha correcta de su reserva ")
        return fecha_reserva

