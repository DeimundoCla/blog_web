from logging import PlaceHolder
from django import forms
from .models import Posteo, Categoria

opciones = Categoria.objects.all().values_list('nome', 'nome')
op = []
for i in opciones:
    op.append(i)

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'categoria', 'autor',]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título hasta 60 caracteres'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un subtítulo hasta 120 caracteres'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue el contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=op, attrs={'class': 'form-control', 'placeholder': 'Seleccione una categoría'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            
        }