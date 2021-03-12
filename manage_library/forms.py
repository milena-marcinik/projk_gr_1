from django.forms import ModelForm

from manage_library.models import Shelf, Book


class ShelfCreateForm(ModelForm):
    class Meta:
        model = Shelf
        fields = ['bookcase', 'name']
        labels = {
            'bookcase': "Room and Bookcase",
            'name': "Shelf name"
        }

class BookAddForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class BookChangeShelfForm(ModelForm):
    class Meta:
        model = Book
        fields = ["shelf"]

class BookChangeShelfForm(ModelForm):
    class Meta:
        model = Book
        fields = ["shelf"]