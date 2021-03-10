from django.forms import ModelForm

from manage_library.models import Shelf


class ShelfCreateForm(ModelForm):
    class Meta:
        model = Shelf
        fields = ['bookcase', 'name']
        labels = {
            'bookcase': "Room and Bookcase",
            'name': "Shelf name"
        }