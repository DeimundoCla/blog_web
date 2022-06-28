from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('post/<slug:url>/', Vistaposteo.as_view(), name='post'),
    path('carga_post/', Cargapost.as_view(), name='cargapost'),
    path('post/<slug:url>/editar_post/', Editarposteo.as_view(), name='editarpost'),
    path('post/<slug:url>/borrar/', Eliminarposteo.as_view(), name='eliminarpost'),
    path('about', about, name="about" ),
    path('404', error , name="404"),
    path('categorias/<str:cate>/', ViewCategoria, name='categoria'),
    path('carga_categoria/', CargaCategoria.as_view(), name='cargacategoria'),
]
