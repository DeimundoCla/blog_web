from django import forms
from .models import Posteo

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            

        }