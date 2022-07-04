from django.contrib import admin
from .models import Comentarios, Posteo, Categoria, Perfil

# Register your models here.

admin.site.register(Posteo)
admin.site.register(Categoria)
admin.site.register(Perfil)
admin.site.register(Comentarios)

