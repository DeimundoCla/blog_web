from django.urls import path
from .views import Vistaposteo, Home, Cargapost

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('post/<int:pk>', Vistaposteo.as_view(), name='post'),
    path('carga_post/', Cargapost.as_view(), name='cargapost'),

]
