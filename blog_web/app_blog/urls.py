from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('post/<slug:url>/', Vistaposteo.as_view(), name='post'),
    path('carga_post/', Cargapost.as_view(), name='cargapost'),
    path('post/<slug:url>/editar_post/', Editarposteo.as_view(), name='editarpost'),
    path('post/<slug:url>/borrar/', Eliminarposteo.as_view(), name='eliminarpost'),
    path('about', AboutView.as_view(), name="about" ),
    path('404', error404 , name="404"),
    path('403', error403 , name="403"),
    path('soporte', soporte , name="soporte"),
    path('categorias/<str:cate>/', ViewCategoria, name='categoria'),
    path('carga_categoria/', CargaCategoria.as_view(), name='cargacategoria'),
    path('like/<slug:url>', LikeView, name='like_post'),
    path('perfil/',PerfilUsuario, name='perfiles'),
    path('post/<slug:url>/comentario/', CargaComentario.as_view(), name='comentario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
