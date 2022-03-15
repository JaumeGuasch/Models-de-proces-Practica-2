from django.urls import path, include
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('lector_register/', views.lector_register.as_view(), name='lector_register'),
    path('periodista_register/', views.periodista_register.as_view(), name='periodista_register'),
]