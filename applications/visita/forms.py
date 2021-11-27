from django import forms
import datetime

from django.forms import widgets
from .models import Visita, Visitantes

class DateInput(forms.DateInput):
    input_type='date'


class visitaForm(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""
    
        model = Visita
        fields = (
            'fecha_visita',
            'usuario',
            'nro_personas'
            
            )
        widgets={
            'fecha_visita': DateInput
        }
        

    def clean_fecha_visita(self):
        

        fecha_actual= datetime.date.today()
        fecha_visita=self.cleaned_data['fecha_visita']
        if fecha_visita<fecha_actual:
            raise forms.ValidationError("ingrese una fecha correcta en su visita ")
        return fecha_visita

    def clean_nro_personas(self):
        nro_personas=self.cleaned_data['nro_personas']
        if nro_personas<1:
            raise forms.ValidationError("ingrese un número correcto de personas ")
        return nro_personas 


class visitantesForm(forms.ModelForm):
    """Form definition for visita."""

    class Meta:
        """Meta definition for visitaform."""

        model = Visitantes
        fields = (
            'dni_visita',
            'nombre_visita',
            'apellido_visita',
            'visita',

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

    # def clean_nro_personas(self):
    #     nro_personas = self.cleaned_data['nro_personas']
    #     if nro_personas < 1:
    #         raise forms.ValidationError(
    #             "ingrese un número correcto de personas ")
    #     return nro_personas
