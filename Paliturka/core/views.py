from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from models import Book
from datetime import datetime


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        today_books = Book.objects.filter(time_created=datetime.today())
        kwargs['today_books'] = today_books
        return kwargs

class CreateBookView(FormView):
    template_name = 'new_book.html'