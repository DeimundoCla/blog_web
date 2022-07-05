from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from .forms import FormRegistro, FormEditarReg
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from app_blog.models import Perfil
from django.contrib.auth.models import User
from django.urls import reverse

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

class EditarProfile(CreateView):
    model = Perfil
    fields = ['info', 'imagen', 'sitio_web', 'instagram_url', 'twitter_url', 'facebook_url', 'user']
    template_name = 'registration/editar_profile.html'
    success_url = reverse_lazy('perfil')
    
    def usuario(self, request, *args, **kwargs):
        form = EditarProfile(request.POST)
        if form.is_valid():
            user_id = self.get_object(user_id)
            form.instance.usuario = request.user
            form.instance.post = user_id
            form.save()
            
    def get_success_url(self):
        return reverse('perfil/')
