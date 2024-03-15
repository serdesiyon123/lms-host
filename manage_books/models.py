from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    rating = models.PositiveIntegerField()
    review = models.TextField()





class Books(models.Model):
    # this should have attributes like Name, Author, Genre, Image etc

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='templates/images')
    description = models.TextField()

    def __str__(self):
        return self.name


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

