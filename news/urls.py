from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import NoticiaList

urlpatterns = [
    path('register/', views.register, name='register'),
    path('lector_register/', views.LectorRegister.as_view(), name='lector_register'),
    path('periodista_register/', views.PeriodistaRegister.as_view(), name='periodista_register'),
    path('login/', views.login_request, name='login'),
    path('home/', login_required(NoticiaList.as_view())),  # força l'usuari a estar autenticat
    path('logout/', views.logout_view, name='logout'),
    path('new/', views.crearnoticia, name='new'),
]
