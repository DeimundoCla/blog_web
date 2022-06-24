from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
    path('registration/registro.html', RegistroUsuario.as_view(), name='registro'),

]