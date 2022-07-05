from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class FormRegistro(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def user_id(self):
        return self.cleaned_data['username']
    
class FormEditarReg(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')