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
