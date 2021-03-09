from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_manage_library, name="main_manage_library"),
    #  wpisalam pojedyncze literki w poniższych ścieżkach, bo chciałam mieć tylko jedną pustą ''
    #  te ponizej do zmiany potem
    path('a/', views.main_manage_library, name="show-book-collection"),
    path('b/', views.main_manage_library, name="add-new-book"),
    path('c/', views.main_manage_library, name="remove-book"),
    path('room/', views.main_manage_library, name="all-rooms"),
    path('d/', views.main_manage_library, name="add-room"),
    path('e/', views.main_manage_library, name="add-bookcase"),
    path('f/', views.main_manage_library, name="add-shelf"),

]
