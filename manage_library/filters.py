import django_filters
from django.utils.translation import ugettext_lazy as _
from .models import Book


class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ('category', 'shelf__bookcase__room')