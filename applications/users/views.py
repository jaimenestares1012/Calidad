from django.shortcuts import render

# Create your views here.

from .forms import UserRegisterForm
from django.views.generic import CreateView


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class =UserRegisterForm
    success_url= '/'