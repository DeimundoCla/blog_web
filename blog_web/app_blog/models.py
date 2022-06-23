from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Posteo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/images', blank=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    

