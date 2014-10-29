from django import forms
from models import Book, Shelf
from djangular.forms import NgFormValidationMixin


class CreateNewBookForm(NgFormValidationMixin, forms.Form):
    form_name = 'create_book'
    name = forms.CharField(label='Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'maxlength': 10000}),
                                  max_length=10000, required=False)
    author = forms.CharField(label='Author', max_length=50)
    genre = forms.CharField(label='Genre', max_length=50)
    status = forms.ChoiceField(label='Status')
    publisher = forms.CharField(label='Publisher', required=False, max_length=50)
    rate = forms.DecimalField(label='Rate', required=False, decimal_places=3, max_digits=3)
    imdb = forms.URLField(label='IMDB', required=False)
    shelf = forms.ChoiceField(label='Shelf')
    country = forms.CharField(label='Country', required=False)
    isbn = forms.CharField(label='ISBN', max_length=14, required=False)
    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super(CreateNewBookForm, self).__init__( *args, **kwargs)
        WILD = 'WILD'
        USED = 'USED'
        BOOK_STATUS = (
            (WILD, 'In the wild'),
            (USED, 'In use')
        )
        self.fields['status'].choices = BOOK_STATUS
        shelfs = list(Shelf.objects.values_list('id', 'address').order_by('address'))
        self.fields['shelf'].choices = shelfs




