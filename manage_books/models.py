from django.db import models


class Status(models.Model):
    # should have relationship with books
    pass


class Rating(models.Model):
    # should have relationship with books
    pass


class Books(models.Model):
    # this should have attributes like Name, Author, Genre, Image etc
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='templates/images')
    def __str__(self):
        return self.name



