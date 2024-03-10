from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterUsers(UserCreationForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2']