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
    rate = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=3)
    imdb = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    feedback = models.ForeignKey('Feedback', null=True, blank=True)
    history = models.ForeignKey('BookHistory', null=True)
    shelf = models.ForeignKey('Shelf')
    genre = models.ForeignKey('Genre')
    publisher = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=14, blank=True, null=True)
    country = models.ForeignKey('Country', blank=True, null=True)
    time_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return ' '.join((self.name, self.author))


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

    def __unicode__(self):
        return self.name


class Feedback(models.Model):
    """
    Feedback model that will store Users comments for Books
    """
    user = models.ForeignKey(FacebookCustomUser, related_name='comments')
    comment = models.TextField(max_length=200)
    time = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.user


class Shelf(models.Model):
    """
    Shelf models. Will indicate location of books in wild
    """
    photo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=50)
    rate = models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True)
    feedback = models.ForeignKey(Feedback, null=True, blank=True)

    def __unicode__(self):
        return self.address


class Genre(models.Model):
    """
    Book genre model
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name