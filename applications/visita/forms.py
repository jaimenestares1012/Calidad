from django import forms
import datetime, time

from django.forms import widgets
from .models import Visita, Visitantes

class DateInput(forms.DateInput):
    input_type='date'


class visita_form(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""
    
        model = Visita
        fields = (
            'fecha_visita',
            'nro_personas'
            
            )
        widgets={
            'fecha_visita': DateInput
        }
        

    def clean_fecha_visita(self):
        fecha_actual= datetime.date.today()
        fecha_actualconhora=datetime.datetime.now()
        hora=fecha_actualconhora.hour
        feckddk=datetime.time(22, 0, 0)
        horamaxima=feckddk.hour
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44", horamaxima, hora)
        
     
        fecha_visita=self.cleaned_data['fecha_visita']
        fecha1 = datetime.date(2023, 1, 1)
        if fecha_visita>fecha1:
            raise forms.ValidationError(
                "ingrese una fecha más proxima, fecha máxima: 2023-01-01")
                
        if fecha_visita<fecha_actual:
            raise forms.ValidationError("ingrese una fecha correcta en su visita ")

        if fecha_actual==fecha_visita:
            print("la fecha a reservar es hoy")
            if hora > horamaxima:
                raise forms.ValidationError(
                    "Muy tarde para registrar una visita, elija otro día")
            
        return fecha_visita

    def clean_nro_personas(self):
        nro_personas=self.cleaned_data['nro_personas']
        if nro_personas<1:
            raise forms.ValidationError("ingrese un número correcto de personas ")
        if nro_personas>25:
            raise forms.ValidationError("Ingrese un número inferior de personas, máximo 25 ")
        return nro_personas 


class visitantes_form(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""

        model = Visitantes
        fields = (
            'dni_visita',
            'nombre_visita',
            'apellido_visita',
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

    def clean_dni_visita(self):
        dni_visita = self.cleaned_data['dni_visita']
        
        print(dni_visita, type(str(dni_visita)))
        if len(str(dni_visita)) != 8:
            print("dentro del ")
            raise forms.ValidationError("ingrese un Dni válido ")
        
        return dni_visita


