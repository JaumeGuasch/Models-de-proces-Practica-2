import datetime
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from django.views.generic import FormView

from .models import Lector, Periodista, Noticia
from news.models import Lector, Periodista, User

now = timezone.now()


class LectorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lector = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.last_login = timezone.now()
        user.save()

        lector = Lector.objects.create(user=user)
        lector.phone_number = self.cleaned_data.get('phone_number')

        lector.save()
        return lector


class PeriodistaSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_periodista = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.last_login = timezone.now()

        user.save()
        periodista = Periodista.objects.create(user=user)
        periodista.phone_number = self.cleaned_data.get('phone_number')

        periodista.save()
        return periodista


# Crear un Noticia form
class CrearNoticia(ModelForm):
    class Meta:
        model = Noticia
        fields = ('titol', 'subtitol', 'cos', 'categoria')

        labels = {
            'titol': 'Introdueix el títol de la notícia',
            'subtitol': 'Introdueix el subtítol de la notícia',
            'cos': 'Introdueix el cos de la notícia',
            'categoria': 'Selecciona una categoria per a la notícia',
        }

        widgets = {
            'titol': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitol': forms.TextInput(attrs={'class': 'form-control'}),
            'cos': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
