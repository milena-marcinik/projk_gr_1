import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label="Title")
    author = django_filters.CharFilter(lookup_expr='icontains', label="Author")

    class Meta:
        model = Book
        fields = ('category', 'shelf__bookcase__room')

    def __init__(self, *args, **kwargs):
        super(BookFilter, self).__init__(*args, **kwargs)
        self.filters['shelf__bookcase__room'].label = "Room"