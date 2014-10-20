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
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(Country, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    shelf = models.ForeignKey(Shelf, blank=True)
    status = models.CharField(max_length=4,
                              choices=BOOK_STATUS,
                              default=WILD)
    rate = models.DecimalField(blank=True)
    history = models.ForeignKey(BookHistory, blank=True)
    feedback = models.ForeignKey(Feedback, blank=True)
    imdb = models.URLField(blank=True)
    image = models.ImageField(blank=True)


class BookHistory(models.Model):
    """
    History model that will display history of book:
    users that have read it, shelf where it live in wild

    """
    #TODO: implement History model
    pass


class Country(models.Model):
    """
    Country model
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    flag = models.ImageField


class Shelf(models.Model):
    """
    Shelf models. Will indicate location of books in wild
    """
    pass


class Feedback(models.Model):
    """
    Feedback model that will store Users comments for Books
    """
    user = models.ForeignKey(FacebookCustomUser, related_name='feedbacks')
    comment = models.TextField(max_length=200)
    time = datetime.now()
    book = models.ManyToManyField(Book, related_name='feedbacks')
