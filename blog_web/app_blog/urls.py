from django.urls import path
from .views import Vistaposteo, Home

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('post/<int:pk>', Vistaposteo.as_view(), name='post'),

]
