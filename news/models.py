from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.views import generic


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
    titol = models.CharField(max_length=200, null=False, default='DEFAULT VALUE')
    subtitol = models.CharField(max_length=400, null=False, default='DEFAULT VALUE')
    cos = models.CharField(max_length=9999999, null=False, default='DEFAULT VALUE')
    periodista = models.ForeignKey(Periodista, default='1', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    valoracio_mitja = models.DecimalField(max_digits=2, decimal_places=1, default='1')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.titol


class Valoracio(models.Model):
    puntuacio = models.IntegerField(default='1', validators=[MaxValueValidator(5), MinValueValidator(1)])
    lector = models.ForeignKey(Lector, default='1', on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, default='1', on_delete=models.CASCADE)
