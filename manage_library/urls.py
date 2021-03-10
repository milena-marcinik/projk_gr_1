from django.urls import path

from . import views
from .views import RoomListView, RoomCreateView, BookcaseListView, BookcaseCreateView, ShelfListView, ShelfCreateView

urlpatterns = [
    path('', views.main_manage_library, name="main_manage_library"),
    #  wpisalam pojedyncze literki w poniższych ścieżkach, bo chciałam mieć tylko jedną pustą ''
    #  te ponizej do zmiany potem
    path('a/', views.main_manage_library, name="show-book-collection"),
    path('b/', views.main_manage_library, name="add-new-book"),
    path('c/', views.main_manage_library, name="remove-book"),
    path('room/', RoomListView.as_view(template_name='manage_library/rooms_all.html'), name="all-rooms"),
    path('addroom/', RoomCreateView.as_view(template_name='manage_library/add_room.html'), name="add-room"),
    path('bookcase/', BookcaseListView.as_view(template_name='manage_library/bookcase_all.html'), name="all-bookcases"),
    path('addbookcase/', BookcaseCreateView.as_view(template_name='manage_library/add_bookcase.html'),
         name="add-bookcase"),
    path('shelf/', ShelfListView.as_view(template_name='manage_library/shelf_all.html'), name="all-shelves"),
    path('addshelf/', ShelfCreateView.as_view(template_name='manage_library/add_shelf.html'), name="add-shelf"),

]
