from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': 'El usuario será el nombre con el que sea identificado en la web'
        }