from django.core.serializers import json
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from models import Book
from datetime import datetime
from forms import CreateNewBookForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        today_books = Book.objects.filter(time_created=datetime.today())
        kwargs['today_books'] = today_books
        return kwargs


class CreateBookView(FormView):
    template_name = 'new_book.html'
    form_class = CreateNewBookForm

    def get_context_data(self, **kwargs):
        context = super(CreateBookView, self).get_context_data(**kwargs)
        context.update(form=CreateNewBookForm())
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_ajax():
            if form.is_valid():
                in_data = json.loads(request.body)