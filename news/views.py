from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView

from .models import User, Lector, Periodista, Noticia
from news.forms import LectorSignUpForm, PeriodistaSignUpForm
from django.utils import timezone


def register(request):
    return render(request, '../templates/register.html')


class LectorRegister(CreateView):
    model = User
    form_class = LectorSignUpForm
    template_name = '../templates/lector_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class PeriodistaRegister(CreateView):
    model = User
    form_class = PeriodistaSignUpForm
    template_name = '../templates/periodista_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/news/home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/news/register')


class NoticiaList(ListView):
    model = Noticia
    template_name = 'home.html'
