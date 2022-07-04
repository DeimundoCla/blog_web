from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('index')

class Posteo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = RichTextField(blank=True)
    imagen = models.ImageField(upload_to='images/')
    categoria = models.CharField(max_length=100, default='General')
    url = models.SlugField(max_length=264, unique=True)
    likes = models.ManyToManyField(User, related_name='like', blank=True)

    def likes_totales(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Posteo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"url": self.url})
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='images/usuarios', blank=True)
    sitio_web = models.CharField(max_length=60, blank=True, verbose_name='Sitio Web')
    instagram_url = models.CharField(max_length=60, default='https://www.instagram.com/', verbose_name="Instagram")
    twitter_url = models.CharField(max_length=60, default='https://www.twitter.com/', verbose_name="Twitter")
    facebook_url = models.CharField(max_length=60, default='https://www.facebook.com/', verbose_name="Facebook")


    def __str__(self):
        return str(self.user)
    
    def retornarusuario(request, self):
        context = {'usuario': self.user}
        return (request, context)

class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posteo, related_name='comentario', on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.first_name + ' | ' + self.usuario.last_name




  

