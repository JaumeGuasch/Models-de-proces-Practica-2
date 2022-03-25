from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from news.forms import LectorSignUpForm, PeriodistaSignUpForm, CrearNoticia
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
class CrearNoticiaView(LoginRequiredMixin,CreateView):
    login_url = '/news/login/'

    template_name = 'new.html'
    form_class = CrearNoticia
    success_url = '/news/home/'

    def noticia_new(self, noticia_id):
        noticia = Noticia.objects.get(pk=noticia_id)
        return render(self, 'new.html', {'noticia': noticia})

    def post(self, request, *args, **kwargs):
        submitted = False
        kwargs = {'user': request.user}
        user_form = CrearNoticia(request.POST or None)

        if not request.user.is_lector:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        if request.method == 'POST' and request.user.is_periodista:
            if user_form.is_valid():
                try:
                    user_form.instance.created_by = request.user
                    user_form.save()
                    return HttpResponseRedirect('/news/new?submitted=True')
                except IntegrityError as err:
                    print('err =>', err)
            else:
                if 'submitted' in request.GET:
                    submitted = True
            return render(request, 'new.html', {'form': user_form, 'submitted': submitted})
