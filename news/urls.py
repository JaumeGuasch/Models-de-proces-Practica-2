from django.urls import path, include
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('lector_register/', views.LectorRegister.as_view(), name='lector_register'),
    path('periodista_register/', views.PeriodistaRegister.as_view(), name='periodista_register'),
]