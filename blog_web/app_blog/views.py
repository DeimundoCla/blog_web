from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Posteo, Categoria, Perfil, Comentarios
from .forms import ComentarioForm, PosteoForm
from usuarios.forms import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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
    #model = Perfil
    #template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        context = super(PerfilUsuario, self).get_context_data(**kwargs)
        context['perfil'] = Perfil.objects.all()
        return context

    def get_object(self):
	    return get_object_or_404(User, pk=self.request.user.id)

 

class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['perfiles'] = Posteo.objects.all()
        return context

class CargaComentario(CreateView):
    model = Comentarios
    template_name = 'comentario.html'
    fields = ['cuerpo', 'post', 'usuario']
    form = ComentarioForm
    
    def comentario(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.usuario = request.user
            form.instance.post = post
            form.save()
            
    def get_success_url(self):
        return reverse('post', kwargs={'url': self.object.post.url})
 
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