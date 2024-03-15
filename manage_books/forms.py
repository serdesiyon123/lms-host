from django.forms import ModelForm
from .models import Books, Rating
from django import forms
class BooksRegister(ModelForm):

    class Meta:
        model = Books
        fields = ['name','author', 'genre', 'poster','description']


class ReviewRegister(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 2}),
        }