from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BooksRegister
from .models import Books
from django.contrib.auth.models import User


@login_required(login_url='/login')
def homepage(request):
    books = Books.objects.all()
    return render(request, 'ui/home.html', {'books': books})

@permission_required('manage_books.add_books', raise_exception=True)
def add_books(request):
    if request.method == 'POST':
        form = BooksRegister(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    elif request.method == 'GET':
        form = BooksRegister()
        return render(request, 'ui/add_books.html', {'form': form})
