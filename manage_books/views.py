from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BooksRegister, ReviewRegister
from .models import Books, Borrow, Rating
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages


def homepage(request):
    if request.method == 'POST':
        delete = request.POST.get('delete')
        if delete:
            book = Books.objects.get(id=delete)
            book.delete()
            return redirect('/home')

    '''filtering by Categories'''
    value = request.GET.get('value')
    if value and value != 'All':
        books = Books.objects.filter(genre=value)
    else:
        books = Books.objects.all()

    borrowed_books = Borrow.objects.all()
    return render(request, 'ui/home.html', {'books': books, 'borrowed_books': borrowed_books})


@permission_required('manage_books.add_books', raise_exception=True)
def update_books(request, id):
    if request.method == 'POST':

        if id == 0:
            form = BooksRegister(request.POST, request.FILES)
        else:
            book = Books.objects.get(pk=id)
            form = BooksRegister(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/home')
    elif request.method == 'GET':

        if id == 0:
            form = BooksRegister()
            return render(request, 'ui/add_books.html', {'form': form})
        else:
            book = Books.objects.get(pk=id)
            form = BooksRegister(instance=book)
        return render(request, 'ui/add_books.html', {'form': form})


def add_books(request):
    if request.method == 'POST':
        form = BooksRegister(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/home')
    elif request.method == 'GET':
        form = BooksRegister()
        return render(request, 'ui/add_books.html', {'form': form})


def admin(request):
    if request.method == 'GET':
        users = User.objects.filter(groups__name='student')
        return render(request, 'ui/admin.html', {'users': users})
    elif request.method == 'POST':
        user_id = request.POST.get('user-id')
        username = request.POST.get('username')

        if user_id:
            user = User.objects.filter(id=user_id).first()
            if request.user.is_staff:
                try:
                    group = Group.objects.get(name='student')
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.get(name='admin')
                    group.user_set.remove(user)
                except:
                    pass
            return redirect('/admin-page')
        elif username:
            user = User.objects.filter(username=username).first()
            if request.user.is_staff:
                admin_group = Group.objects.get(name='admin')
                student_group = Group.objects.get(name='student')
                admin_group.user_set.add(user)
                student_group.user_set.remove(user)
            return redirect('/admin-page')


def search_result(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search is not None:
            books = Books.objects.filter(
                Q(name__icontains=search) | Q(author__icontains=search) | Q(genre__icontains=search))
            return render(request, 'ui/search.html', {'books': books})
        else:
            return render(request, 'ui/home.html')




def search_users(request):
    if request.method == 'GET':
        search_user = request.GET.get('search-user')
        Users = User.objects.all()
        users = Users.objects.filter(username__icontains=search_user)
        return render(request, 'ui/search_users.html', {'users': users})
    return render(request, 'ui/search_users.html', )


@login_required(login_url='/status')
def status(request):
    borrowed = Borrow.objects.filter(user=request.user)
    return render(request, 'ui/status.html', {'borrowed': borrowed})


def borrow(request, book_id):
    if request.method == 'GET':
        max_limit = 3

        count = Borrow.objects.filter(user=request.user).count()

        if count >= max_limit:
            messages.error(request,"You have reached max book limit \n please return some book to take more")
            return redirect('/status')
        book = Books.objects.get(id=book_id)
        Borrow.objects.create(
            id=book_id,
            book=book,
            user=request.user,
            borrow_date=timezone.now(),
            return_date=timezone.now() + timedelta(weeks=2)
        )
        return redirect('description-each', id=book_id)


def return_book(request, book_id):
    if request.method == 'GET':
       book = Borrow.objects.get(pk=book_id)
       book.delete()
       return redirect('status')

def description(request,id):
    if request.method == 'GET':
        review = ReviewRegister()
        user_reviews = Rating.objects.all()
        book = Books.objects.get(pk=id)
        taken = Borrow.objects.all().values_list('book__id', flat=True)
        user_borrowed = Borrow.objects.filter(user=request.user,book=book).exists()
        return render(request, 'ui/description.html', {'book':book , 'taken': taken, 'user_borrowed':user_borrowed,'review': review, 'user_reviews': user_reviews})

    elif request.method == 'POST':
        review_form= ReviewRegister(request.POST)
        book = Books.objects.get(pk=id)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = book
            review.review_date = timezone.now()
            review.id = id
            review.save()
        return redirect('description-each', id=id)
