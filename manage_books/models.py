from django.db import models


class Books(models.Model):
    # this should have attributes like Name, Author, Genre, Image etc
    pass


class Status(models.Model):
    # should have relationship with books
    pass


class Rating(models.Model):
    # should have relationship with books
    pass
