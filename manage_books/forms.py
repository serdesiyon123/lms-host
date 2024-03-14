from django.forms import ModelForm
from .models import Books

class BooksRegister(ModelForm):

    class Meta:
        model = Books
        fields = ['name','author', 'genre', 'poster','description']