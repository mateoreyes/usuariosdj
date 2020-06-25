from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from .models import User

class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleanned_data['username'],
            form.cleanned_data['email'],
            form.cleanned_data['password1'],
            # datos extra
            nombres = form.cleanned_data['nombres'],
            apellidos = form.cleanned_data['apellidos'],
            genero = form.cleanned_data['genero'],
        )
        return super(UserRegisterForm, self).form_valid(form)

class HomePage(TemplateView):
    template_name = "users/index.html"