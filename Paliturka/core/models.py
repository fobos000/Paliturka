from datetime import datetime
from django.db import models
from django_facebook.models import FacebookCustomUser
# Create your models here.


class Book(models.Model):
    """
    Basic book model
    """
    WILD = 'WILD'
    USED = 'USED'
    BOOK_STATUS = (
        (WILD, 'In the wild'),
        (USED, 'In use')
    )

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=4,
                              choices=BOOK_STATUS,
                              default=WILD)
    rate = models.DecimalField(blank=True, decimal_places=3, max_digits=3)
    imdb = models.URLField(blank=True)
    image = models.ImageField(blank=True)
    feedback = models.ForeignKey('Feedback')
    history = models.ForeignKey('BookHistory')
    book = models.ForeignKey('Shelf')
    genre = models.ForeignKey('Genre')
    publisher = models.ForeignKey('Publisher')
    author = models.ForeignKey('Author')


class BookHistory(models.Model):
    """
    History model that will display history of book:
    users that have read it, shelf where it live in wild

    """
    user = models.ForeignKey(FacebookCustomUser)
    start_date = models.DateField()
    end_date = models.DateField()


class Country(models.Model):
    """
    Country model
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    flag = models.ImageField(blank=True)


class Feedback(models.Model):
    """
    Feedback model that will store Users comments for Books
    """
    user = models.ForeignKey(FacebookCustomUser, related_name='comments')
    comment = models.TextField(max_length=200)
    time = datetime.now()


class Shelf(models.Model):
    """
    Shelf models. Will indicate location of books in wild
    """
    photo = models.ImageField(blank=True)
    address = models.CharField(max_length=50)
    rate = models.DecimalField(blank=True, decimal_places=3, max_digits=3)
    feedback = models.ForeignKey(Feedback)


class Genre(models.Model):
    """
    Book genre model
    """
    name = models.CharField(max_length=50)


class Publisher(models.Model):
    """
    Book publisher model
    """
    name = models.CharField(max_length=50)


class Author(models.Model):
    """
    Book author model
    """
    name = models.CharField(max_length=100)