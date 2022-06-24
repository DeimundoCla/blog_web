from django import forms
from .models import Posteo

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título hasta 60 caracteres'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un subtítulo hasta 120 caracteres'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue el contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            

        }