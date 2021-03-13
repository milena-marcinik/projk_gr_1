from django_filters import FilterSet

from .models import Book


class BookFilter(FilterSet):

    class Meta:
        model = Book
        fields = ('category', 'shelf', 'title')