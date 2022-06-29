from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/registro.html', RegistroUsuario.as_view(), name='registro'),
    path('registration/editar_perfil.html', EditarPerfil.as_view(), name='editar_perfil'),
    path('password/', CambiarPass.as_view(template_name='registration/change-password.html'), name='password'), 
]