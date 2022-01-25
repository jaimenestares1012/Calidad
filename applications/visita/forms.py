from msilib.schema import LockPermissions
from django import forms
import datetime, time

from django.forms import widgets
from .models import Visita, Visitantes

# se crea el date input
class DateInput(forms.DateInput):
    # tipo date en el type
    input_type='date'

# se crea el form en el form
class visita_form(forms.ModelForm):
    """Form definition for visita."""
    # se define un meta
    class Meta:
        """Meta definition for visitaform."""
        # se determina en un model
        model = Visita
        # se crea los fields a usar
        fields = (
            'fecha_visita',
            'nro_personas'
            
            )
        # se crea la fecha y su formato
        widgets={
            'fecha_visita': DateInput
        }
        

    # se crea el clean fecha para la validacion
    def clean_fecha_visita(self):
        # se crea la fecha actual
        fecha_actual= datetime.date.today()
        # se invoca el datetime 
        fecha_actualconhora=datetime.datetime.now()
        # se crea la hora actual
        hora=fecha_actualconhora.hour
        feckddk=datetime.time(22, 0, 0)
        # se crea una hora maxima
        horamaxima=feckddk.hour
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44", horamaxima, hora)
        
     
        fecha_visita=self.cleaned_data['fecha_visita']
        # se crea un date time para el 2023
        fecha1 = datetime.date(2023, 1, 1)
        # se crea un da43434a el 2023
        if fecha_visita>fecha1:
            raise forms.ValidationError(
                "ingrese una fecha más proxima, fecha máxima: 2023-01-01")
        # se crea43me para elecf      
        if fecha_visita<fecha_actual:
            raise forms.ValidationError("ingrese una fecha correcta en su visita ")
        # se crea un date time para el 2023
        if fecha_actual==fecha_visita:
            print("la fecha a reservar es hoy")
            if hora > horamaxima:
                raise forms.ValidationError(
                    "Muy tarde para registrar una visita, elija otro día")
        # se retorna la fecha de visita 
        return fecha_visita
    # se hace el filtro del nro de personas
    def clean_nro_personas(self):
        # se extrae el nro de personas
        nro_personas=self.cleaned_data['nro_personas']
        # se hace la decision
        if nro_personas<1:
            raise forms.ValidationError("ingrese un número correcto de personas ")
            # se muestra el mensajhe
        if nro_personas>25:
            raise forms.ValidationError("Ingrese un número inferior de personas, máximo 25 ")
            # se crea un date time para el 2023
        return nro_personas 

# se define un form
class visitantes_form(forms.ModelForm):
    """Form definition for visita."""
    # se crea un meta
    class Meta:
        """Meta definition for visitaform."""
        # se determina un modelo que se tomara como ejemolo 
        model = Visitantes
        fields = (
            'dni_visita',
            'nombre_visita',
            'apellido_visita',
        )
       
    # se crea el fitro pa dni23
    def clean_dni_visita(self):
        dni_visita = self.cleaned_data['dni_visita']
        # se determina el tamaño ime para el 2023
        print(dni_visita, type(str(dni_visita)))
        if len(str(dni_visita)) != 8:
            print("dentro del ")
            raise forms.ValidationError("ingrese un Dni válido ")
        # se RETORNA visita
        return dni_visita


