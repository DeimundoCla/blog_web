from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Perfil, Posteo, Categoria
from .forms import PosteoForm, PerfilForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
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

    def get_context_data(self, **kwargs):
        context = super(Vistaposteo, self).get_context_data(**kwargs)

        likes = get_object_or_404(Posteo, url=self.kwargs['url'])
        likes_tot = likes.likes_totales()
        context['likes_totales'] = likes_tot
        return context

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

class PerfilUsuario(DetailView):
    model = Perfil
    template_name = 'perfil.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


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

def LikeView(request, url):
    post = get_object_or_404(Posteo, url=request.POST.get('posteo_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', kwargs={'url': url}))