from django import forms
import datetime

from django.forms import widgets
from .models import trabajo_mantenimiento, Externos


class DateInput(forms.DateInput):
    input_type = 'date'


class my_mantenimiento_form(forms.ModelForm):
    print("dentro del form")

    class Meta:

        model = trabajo_mantenimiento
        fields = (
            'nro_trabajadores',
            'dia_mantenimiento',
            'hora_mantenimiento',
            'descripcion',
           
        )
        widgets = {
            'dia_mantenimiento': DateInput
        }   

    print("ates del clean fecha reserva")

    def clean_dia_mantenimiento(self):
        print("dentro del  fecha reserva")   
        fecha_actual = datetime.date.today()
        print("esta es la fecha actual", fecha_actual)
        fecha_reserva = self.cleaned_data['dia_mantenimiento']
        print("esta es la fecha de reserva en el forms", fecha_reserva)
        print(type(fecha_reserva))
        fecha1 = datetime.date(2023, 1, 1)
        if fecha_reserva > fecha1:
            raise forms.ValidationError("ingrese una fecha más proxima, fecha máxima: 2023-01-01")
        print(type(fecha1))
        # fecha_reserva=fecha_reserva.split("-")
        print("wdeidiededede", fecha_reserva)
        if fecha_reserva < fecha_actual:
            raise forms.ValidationError("ingrese una fecha correcta de su reserva ")

        return fecha_reserva


class ExternosForm(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""

        model = Externos
        fields = (
            'dni_externo',
            'nombre_externo',
            'apellido_externo',
        
        )
        # widgets = {
        #     'dni_visita': in
        # }

    # def clean_fecha_visita(self):

    #     fecha_actual = datetime.date.today()
    #     fecha_visita = self.cleaned_data['fecha_visita']
    #     if fecha_visita < fecha_actual:
    #         raise forms.ValidationError(
    #             "ingrese una fecha correcta en su visita ")
    #     return fecha_visita

    def clean_dni_externo(self):
        dni_visita = self.cleaned_data['dni_externo']

        print(dni_visita, type(str(dni_visita)))
        if len(str(dni_visita)) != 8:
            print("dentro del ")
            raise forms.ValidationError("ingrese un Dni válido ")

        return dni_visita
