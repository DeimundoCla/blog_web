from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posteo, Categoria
from .forms import PosteoForm
from django.http import HttpResponse
from django.template import loader
# Create your views here.

class Home(ListView):
    model = Posteo
    template_name = 'index.html'
    ordering = ['-fecha_publicacion']

class Vistaposteo(DetailView):
    model = Posteo
    template_name = 'post.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'

class CargaCategoria(CreateView):
    model = Categoria
    template_name = 'carga_categoria.html'
    fields = ['nome']

class Cargapost(CreateView):
    model = Posteo
    form_class = PosteoForm
    template_name = 'carga_post.html'

class Editarposteo(UpdateView):
    model = Posteo
    template_name = 'editar_post.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'categoria', 'url']
    slug_field = 'url'
    slug_url_kwarg = 'url'

class Eliminarposteo(DeleteView):
    model = Posteo
    template_name = 'eliminar_post.html'
    success_url = '/'
    slug_field = 'url'
    slug_url_kwarg = 'url'


def about(request):
    template = loader.get_template("about.html")
    documento = template.render()
    return HttpResponse(documento)

def error(request):
    template = loader.get_template("404.html")
    documento = template.render()
    return HttpResponse(documento)

def ViewCategoria(request, cate):
    post_cats = Posteo.objects.filter(categoria = cate.replace('-', ' '))
    return render(request, 'categorias.html', {'cate': cate.title().replace('-', ' '), 'post_cats': post_cats})