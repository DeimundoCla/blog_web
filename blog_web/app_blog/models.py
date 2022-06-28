from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
            
    def get_absolute_url(self):
        return reverse('index')

class Posteo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/images', blank=True)
    categoria = models.CharField(max_length=100, default='General')
    url = models.SlugField(max_length=264, unique=True, null=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Posteo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"url": self.url})
    

    

    

