from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('lector_register/', views.LectorRegister.as_view(), name='lector_register'),
    path('periodista_register/', views.PeriodistaRegister.as_view(), name='periodista_register'),
    path('login/', views.login_request, name='login'),
    path('home/', views.NoticiaList.as_view(), name='home'),  # força l'usuari a estar autenticat
    path('logout/', views.logout_view, name='logout'),
    path('new/', views.CrearNoticiaView.as_view(), name='new'),
]
