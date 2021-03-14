import isbnlib
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


class BookAddISBNForm(ModelForm):
    class Meta:
        model = Book
        fields = ["isbn_number"]

    def save(self):
        print("XXXXXXXXXX")
        print(self.cleaned_data['isbn_number'])
        print(isbnlib.meta(self.cleaned_data['isbn_number'])['Title'])
        print("POOOOO")
        new_book = Book.objects.create(
            # isbn_number = self.cleaned_data['isbn_number'],
            # title=isbnlib.meta(self.isbn_number)['Title'],
            # author=isbnlib.meta(self.isbn_number)['Authors'],
            # # cover=isbnlib.meta(self.isbn_number),
        )

        return new_book

    # import isbnlib
    #
    # isbn = '9788177581805'
    #
    # book = isbnlib.meta(isbn)
    #
    # title = book['Title']
    # authors = book['Authors']


class BookChangeShelfForm(ModelForm):
    class Meta:
        model = Book
        fields = ["shelf"]


class BookUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'note', 'category']

    # def save(self, commit=True):
    #     super().save()
    #     book = super(BookUpdateForm, self).save(commit=False)
    #     book.cover = self.cleaned_data["cover"]
    #     book.title = self.cleaned_data["title"]
    #     book.author = self.cleaned_data["author"]
    #     if commit:
    #         book.save()
    #     return book
