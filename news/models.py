from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model
from django.forms import ModelForm
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    is_periodista = models.BooleanField(default=False)
    is_lector = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Periodista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False, default='DEFAULT VALUE')
    last_login = models.DateTimeField(default=timezone.now())


class Lector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False, default='DEFAULT VALUE')
    last_login = models.DateTimeField(default=timezone.now())


CATEGORIA_CHOICES = [
    (1, 'Política'),
    (2, 'Economia'),
    (3, 'Social'),
    (4, 'Esports'),
    (5, 'Opinió'),
    (6, 'Successos'),
]


class Noticia(models.Model):
    titol = models.CharField(max_length=200, null=False, default='DEFAULT VALUE')
    subtitol = models.CharField(max_length=400, null=False, default='DEFAULT VALUE')
    cos = models.CharField(max_length=9999999, null=False, default='DEFAULT VALUE')
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES, default='Sense categoria')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    valoracio_mitja = models.DecimalField(max_digits=2, decimal_places=1, default='0')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.titol


class Valoracio(models.Model):
    puntuacio = models.IntegerField(default='1', validators=[MaxValueValidator(5), MinValueValidator(1)])
    lector = models.ForeignKey(Lector, default='1', on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, default='1', on_delete=models.CASCADE)


class SubmitNoticia(ModelForm):
    class meta:
        model = Noticia
        fields = ['titol', 'subtitol', 'cos', 'categoria']
