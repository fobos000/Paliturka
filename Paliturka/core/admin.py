from django.contrib import admin
from django.core.exceptions import ValidationError
from models import Book, Shelf, Genre, Country
from django.templatetags.static import static
from django import forms
from django.utils.safestring import mark_safe


class AdminImageWidget(forms.FileInput):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<div style="float:left"><a target="_blank" href="%s">'
                           '<img src="%s" style="height: 120px;" /></a><br> '
                           % (static(value.url), static(value.url))))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        output.append('</div>')
        return mark_safe(u''.join(output))


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {'image': AdminImageWidget}

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if hasattr(image, '_size') and image._size > 5 * 1024 * 1024:
                raise ValidationError("Image file size is larger than 5mb")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

    exclude = ('history', 'feedback')


class ShelfAdmin(admin.ModelAdmin):
    exclude = ('feedback', )


class GenreAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Country, CountryAdmin)