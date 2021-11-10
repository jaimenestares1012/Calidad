from django.shortcuts import render

# Create your views here.

from .forms import UserRegisterForm
from .models import User
from django.views.generic.edit import FormView


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class =UserRegisterForm
    success_url= '/'

    def form_valid(self, form) :
      
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
        )
        return super(UserRegisterView, self).form_valid(form)