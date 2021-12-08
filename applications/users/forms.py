from django import forms
from django.forms import fields
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
       
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2=forms.CharField(
       
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        abstract = True
        model=User
        fields = (
            'username',
            'email',
            'password1'
            )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    username = forms.CharField(
        
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
            }
        )
    )
    password = forms.CharField(
        
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean() 
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Los datos de usuario no son correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
       
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
