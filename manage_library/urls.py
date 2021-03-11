from django.urls import path
from django.views.generic import DetailView

from . import views
from .models import Book
from .views import RoomListView, RoomCreateView, BookcaseListView, BookcaseCreateView, ShelfListView, ShelfCreateView, \
    BookAddView, BookListView



urlpatterns = [
    path('', views.main_manage_library, name="main_manage_library"),
    #  wpisalam pojedyncze literki w poniższych ścieżkach, bo chciałam mieć tylko jedną pustą ''
    #  te ponizej do zmiany potem
    path('listallbooks/', BookListView.as_view(template_name="manage_library/books_all.html"), name="list-all-books"),

        path('detailsbook/<int:pk>', DetailView.as_view(model=Book), name="show-book-details"),

    path('addnewbook/', BookAddView.as_view(template_name="manage_library/add_book.html"), name="add-new-book"),
    path('c/', views.main_manage_library, name="remove-book"),
    path('room/', RoomListView.as_view(template_name='manage_library/rooms_all.html'), name="all-rooms"),
    path('addroom/', RoomCreateView.as_view(template_name='manage_library/add_room.html'), name="add-room"),
    path('bookcase/', BookcaseListView.as_view(template_name='manage_library/bookcase_all.html'), name="all-bookcases"),
    path('addbookcase/', BookcaseCreateView.as_view(template_name='manage_library/add_bookcase.html'),
         name="add-bookcase"),
    path('shelf/', ShelfListView.as_view(template_name='manage_library/shelf_all.html'), name="all-shelves"),
    path('addshelf/', ShelfCreateView.as_view(template_name='manage_library/add_shelf.html'), name="add-shelf"),

]
