from django.shortcuts import render
from django.views import generic
from .forms import FormRegistro
from django.urls import reverse_lazy


# Create your views here.

class RegistroUsuario(generic.CreateView):
    form_class = FormRegistro
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')