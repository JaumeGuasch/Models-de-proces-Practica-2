from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
# Falta: classe valoració, periodista com a foreign key de Noticia

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
    periodista = models.ForeignKey(Periodista, default='', on_delete=models.CASCADE)


class Valoracio(models.Model):
    puntuacio = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    lector = models.ForeignKey(Noticia, default=1, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Lector, default='', on_delete=models.CASCADE)
