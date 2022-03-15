from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    is_periodista = models.BooleanField(default=False)
    is_lector = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Periodista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False, default='DEFAULT VALUE')


class Lector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False, default='DEFAULT VALUE')


class Noticia(models.Model):
    titol = models.CharField(max_length=20, null=False, default='DEFAULT VALUE')
    subtitol = models.CharField(max_length=120, null=False, default='DEFAULT VALUE')
    cos = models.CharField(max_length=99999, null=False, default='DEFAULT VALUE')
