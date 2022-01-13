from django import forms
import datetime

from django.forms import widgets
from .models import trabajo_mantenimiento, Externos

# se crea el form para los inppyut date
class DateInput(forms.DateInput):
    input_type = 'date'

# se creal el form para el modelos trabajmo_mantenimeinto
class my_mantenimiento_form(forms.ModelForm):
    print("dentro del form")
    # se crea la clase meta
    class Meta: 
        # invocamos el modelo
        model = trabajo_mantenimiento
        # invocamos los inputs que infresará el usuario
        fields = (
            'nro_trabajadores',
            'dia_mantenimiento',
            'hora_mantenimiento',
            'descripcion',
            'nro_departamento'
           
        )
        # se define el tipo de date input 
        widgets = {
            'dia_mantenimiento': DateInput
        }   

    print("ates del clean fecha reserva")
    # se crea el dia mantemimiento para que pueda ser validado
    def clean_dia_mantenimiento(self):
        print("dentro del  fecha reserva")   
        fecha_actual = datetime.date.today()
        print("esta es la fecha actual", fecha_actual)
        fecha_reserva = self.cleaned_data['dia_mantenimiento']
        print("esta es la fecha de reserva en el forms", fecha_reserva)
        print(type(fecha_reserva))
        # se obtiene la fecha actual
        fecha1 = datetime.date(2023, 1, 1)
        # se hace las comparaciones

        if fecha_reserva > fecha1:
            # se muestra el mensjae de validacion
            raise forms.ValidationError("ingrese una fecha más proxima, fecha máxima: 2023-01-01")
        print(type(fecha1))
        # fecha_reserva=fecha_reserva.split("-")

        print("wdeidiededede", fecha_reserva)
        # se intenta validar la faecha ingresada
        if fecha_reserva < fecha_actual:
            # se muestra los mendajes de validacion

            raise forms.ValidationError("ingrese una fecha correcta de su reserva ")
        # se retorna si es que ha pasado por todas las validaciones
        return fecha_reserva

# se crea el form externos
class ExternosForm(forms.ModelForm):
    """Form definition for visita."""
    # se cre el meta para el form
    class Meta:
        """Meta definition for visitaform."""
        # definimos el modelo a usar
        model = Externos
        # definomos los fields
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

    # definimos el clean para el dni y su validacion
    def clean_dni_externo(self):
        dni_visita = self.cleaned_data['dni_externo']
        # hace el conteo de caracteres
        print(dni_visita, type(str(dni_visita)))
        # se hace la decision
        if len(str(dni_visita)) != 8:
            # esta dento de un dni invalido
            print("dentro del ")
            raise forms.ValidationError("ingrese un Dni válido ")
        # paso la validacion
        print( dni_visita )
        # se retorna el dni visira
        return dni_visita
