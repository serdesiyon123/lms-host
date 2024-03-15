from django.contrib import admin
from .models import Books,Borrow,Rating


class BooksAdmin(admin.ModelAdmin):
    list = ('id','name','author', 'description')

admin.site.register(Books,BooksAdmin)
admin.site.register(Borrow)
admin.site.register(Rating)