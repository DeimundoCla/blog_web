from django.urls import path
from .views import Editarposteo, Vistaposteo, Home, Cargapost, Eliminarposteo

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('post/<int:pk>', Vistaposteo.as_view(), name='post'),
    path('carga_post/', Cargapost.as_view(), name='cargapost'),
    path('post/editar_post/<int:pk>', Editarposteo.as_view(), name='editarpost'),
    path('post/<int:pk>/borrar', Eliminarposteo.as_view(), name='eliminarpost'),

]
