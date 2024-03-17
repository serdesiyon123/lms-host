from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




class Books(models.Model):
    # this should have attributes like Name, Author, Genre, Image etc
    GENRE_CHOICES = [
        ('fic','Fiction'),
        ('non-fic','Non-Fiction'),
        ('my','Mystery'),
        ('rom','Romance'),
        ('sci-fi','Science Fiction'),
        ('hi-fi','Historical Fiction'),
        ('ch-lit','Childers Literature'),
    ]

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES)
    poster = models.ImageField(upload_to='templates/images')
    description = models.TextField()

    def __str__(self):
        return self.name


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)


class Rating(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review = models.TextField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)