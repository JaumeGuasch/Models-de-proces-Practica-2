from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Lector, Periodista

from news.models import Lector, Periodista, User


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
        user.save()

        lector = Lector.objects.create(user=user)
        lector.phone_number =self.cleaned_data.get('phone_number')
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
        user.save()
        periodista = Periodista.objects.create(user=user)
        periodista.phone_number =self.cleaned_data.get('phone_number')
        periodista.save()
        return periodista


