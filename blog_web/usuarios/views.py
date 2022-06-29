from django.shortcuts import render
from django.views import generic
from .forms import FormRegistro, FormEditarReg
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class RegistroUsuario(generic.CreateView):
    form_class = FormRegistro
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class EditarPerfil(generic.CreateView):
    form_class = FormEditarReg
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
    
class CambiarPass(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('index')
