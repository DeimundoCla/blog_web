from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posteo
from .forms import PosteoForm

# Create your views here.

class Home(ListView):
    model = Posteo
    template_name = 'index.html'
    ordering = ['-fecha_publicacion']

class Vistaposteo(DetailView):
    model = Posteo
    template_name = 'post.html'

class Cargapost(CreateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'carga_post.html'

class Editarposteo(UpdateView):
    model = Posteo
    template_name = 'editar_post.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

class Eliminarposteo(DeleteView):
    model = Posteo
    template_name = 'eliminar_post.html'
    success_url = '/'