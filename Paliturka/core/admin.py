from django.contrib import admin
from models import Book


class BookAdmin(admin.ModelAdmin):
        fields = (
            'name', 'description', 'status', 'rate', 'imdb', 'image',
        )

admin.site.register(Book, BookAdmin)