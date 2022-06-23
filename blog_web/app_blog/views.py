from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posteo
from .forms import PosteoForm

# Create your views here.

class Home(ListView):
    model = Posteo
    template_name = 'index.html'

class Vistaposteo(DetailView):
    model = Posteo
    template_name = 'post.html'

class Cargapost(CreateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'carga_post.html' 