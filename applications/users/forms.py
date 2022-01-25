from django import forms
from django.forms import fields
from django.contrib.auth import authenticate
from .models import User
# se crea el form del registro 
class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
       # se crea el passoord a usar
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    # se da valores al segunfo pass
    password2=forms.CharField(
       
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )
    # se determina una meta a teenr
    class Meta:
        # se crea el abstract true
        abstract = True
        # se determina el modelo
        model=User
        # sus respectivos filtrs
        fields = (
            'username',
            'email',
            'password1'
            )
    # se creal password y que sean iguales
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

# se crea la clase loggin
class LoginForm(forms.Form):
    # se crea un username con sus paremtros
    username = forms.CharField(
        
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
            }
        )
    )
    # see extrae el password
    password = forms.CharField(
        
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña'
            }
        )
    )
    # se hace la limpieza de los clean
    def clean(self):
        # se invoca la funcion super
        cleaned_data = super(LoginForm, self).clean() 
        print(cleaned_data)
        # se tiene el username y el password
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        # se hace la validacion si no esta auntenticado
        if not authenticate(username=username, password=password):
            # se muestra el mensaje de error
            raise forms.ValidationError(
                'Los datos de usuario no son correctos')

        return self.cleaned_data

# se creal el password y sus plachejolder
class UpdatePasswordForm(forms.Form):
    # se tiene el 1er pass y se le da un required
    password1 = forms.CharField(
       
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    # se tiene el 2do pass
    password2 = forms.CharField(
        
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
