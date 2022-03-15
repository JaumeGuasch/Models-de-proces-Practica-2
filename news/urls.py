from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('lector_register/', views.LectorRegister.as_view(), name='lector_register'),
    path('periodista_register/', views.PeriodistaRegister.as_view(), name='periodista_register'),
    path('login/', views.login_request, name='login'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),

]
