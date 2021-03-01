from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_manage_library, name="main_manage_library"),
    path('', views.main_manage_library, name="show-book-collection"),
    path('', views.main_manage_library, name="add-new-book"),
    path('', views.main_manage_library, name="remove-book"),
    path('', views.main_manage_library, name="add-bookcase"),
]