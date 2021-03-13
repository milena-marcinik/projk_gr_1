import django_filters
from django.utils.translation import ugettext_lazy as _
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('category', 'shelf__bookcase__room')