from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('add/', views.add_books, name='add_books'),
    path('update/<int:id>', views.update_books, name='update_books'),
    path('admin-page/', views.admin, name='admin-page'),
    path('search/', views.search_result, name='search'),
    path('search-users/', views.search_users, name='search-users'),
    path('status/', views.status, name='status'),
    path('borrow/<int:book_id>', views.borrow, name='borrow'),
    path('return_book/<int:book_id>', views.return_book, name='return_books'),
    path('description/', views.description, name='description'),
    path('description/<int:id>', views.description, name='description-each'),



]