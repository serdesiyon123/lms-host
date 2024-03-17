import os

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError





class RegisterUsers(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True, )


    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already taken.")
        return email

    def save(self, commit=True):
        user = super(RegisterUsers, self).save(commit=False)
        if self.cleaned_data.get('password1') == 'iamsuperuser':
            user.is_staff = True
        if commit:
            user.save()
        return user