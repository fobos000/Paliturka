from django import forms
from models import Book, Shelf


class CreateNewBookForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 10000}),
                                  max_length=10000, required=False)
    author = forms.CharField(max_length=50)
    genre = forms.CharField(max_length=50)
    status = forms.ChoiceField()
    publisher = forms.CharField(required=False, max_length=50)
    rate = forms.DecimalField(required=False, decimal_places=3, max_digits=3)
    imdb = forms.URLField(required=False)
    shelf = forms.ChoiceField()
    country = forms.CharField(required=False)
    isbn = forms.CharField(max_length=14, required=False)
    image = forms.ImageField(required=False)

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




