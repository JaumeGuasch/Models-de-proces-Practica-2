from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from news.forms import LectorSignUpForm, PeriodistaSignUpForm, CrearNoticia
from .decorators import lector_required
from .models import User, Noticia


def register(request):
    return render(request, '../templates/register.html')


class LectorRegister(CreateView):
    model = User
    form_class = LectorSignUpForm
    template_name = '../templates/lector_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/news/login')


class PeriodistaRegister(CreateView):
    model = User
    form_class = PeriodistaSignUpForm
    template_name = '../templates/periodista_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/news/login')


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
    return redirect('/')


class NoticiaList(LoginRequiredMixin, ListView):
    login_url = '/news/login/'
    model = Noticia
    template_name = 'home.html'


###################################
class CrearNoticiaView(LoginRequiredMixin, CreateView):
    template_name = 'new.html'
    form_class = CrearNoticia
    success_url = '/news/home/'

    @method_decorator(login_required())
    def periodista_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/news/login'):
        actual_decorator = user_passes_test(
            lambda u: u.is_active and u.is_periodista,
            login_url=login_url,
            redirect_field_name=redirect_field_name
        )
        if function:
            return actual_decorator(function)
        return actual_decorator

    def post(self, request, *args, **kwargs):
        if request.user.is_lector:
            return HttpResponseRedirect('/news/unauthorized')
        else:
            if request.method == 'POST':
                user_form = CrearNoticia(request.POST)
                if user_form.is_valid():
                    user_form.instance.created_by = request.user
                    user_form.save()
                    return HttpResponseRedirect('/news/submitted')





