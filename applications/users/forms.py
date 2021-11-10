from django import forms
from django.forms import fields

from .models import User

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2=forms.CharField(
        label='Contraseña',
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
            )