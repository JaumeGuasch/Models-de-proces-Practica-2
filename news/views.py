from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User, Lector, Periodista
from news.forms import LectorSignUpForm, PeriodistaSignUpForm


def register(request):
    return render(request, '../templates/register.html')


class lector_register(CreateView):
    model = User
    form_class = LectorSignUpForm
    template_name = '../templates/lector_register.html'

class periodista_register(CreateView):
    model = User
    form_class = PeriodistaSignUpForm
    template_name = '../templates/periodista_register.html'
