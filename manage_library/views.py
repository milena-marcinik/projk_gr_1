from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from manage_library.forms import ShelfCreateForm, BookAddForm, BookChangeShelfForm
from manage_library.models import Room, Bookcase, Shelf, Book


class MainManageLibrary(ListView):
    model = Book
    context_object_name = 'books_all'  # your own name for the list as a template variable
    queryset = Book.objects.all()
    ordering = ['-date_added']
    template_name = 'manage_library/main_manage_library.html'  # Specify your own template name/location


class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms_all'  # your own name for the list as a template variable
    queryset = Room.objects.all()
    template_name = 'manage_library/rooms_all.html'  # Specify your own template name/location


class RoomCreateView(SuccessMessageMixin, CreateView):
    model = Room
    fields = ['name']
    success_url = '/room/'
    success_message = "New room created!"

    def form_valid(self, form):
        return super().form_valid(form)


class BookcaseListView(ListView):
    model = Bookcase
    context_object_name = 'bookcases_all'  # your own name for the list as a template variable
    queryset = Bookcase.objects.all()
    template_name = 'manage_library/bookcase_all.html'  # Specify your own template name/location


class BookcaseCreateView(SuccessMessageMixin, CreateView):
    model = Bookcase
    fields = ['room', 'name']
    success_url = '/bookcase/'
    success_message = "New bookcase created!"

    def form_valid(self, form):
        return super(BookcaseCreateView, self).form_valid(form)


class ShelfListView(ListView):
    model = Shelf
    context_object_name = 'shelves_all'  # your own name for the list as a template variable
    queryset = Shelf.objects.all()
    template_name = 'manage_library/shelf_all.html'  # Specify your own template name/location


class ShelfCreateView(SuccessMessageMixin, CreateView):
    form_class = ShelfCreateForm
    success_url = '/shelf/'
    success_message = "New shelf created!"

    def form_valid(self, form):
        return super(ShelfCreateView, self).form_valid(form)


class BookAddView(SuccessMessageMixin, CreateView):
    form_class = BookAddForm
    success_url = "/addnewbook/"
    success_message = "New book added to library"

    def form_valid(self, form):
        return super().form_valid(form)


class BookListView(ListView):
    model = Book
    context_object_name = 'books_all'
    queryset = Book.objects.all()


class BooksDeleteView(SuccessMessageMixin, DeleteView):
    model = Book
    success_message = "Book removed"
    success_url = '/listallbooks/'


def change_book_status(request, pk):
    picked_book = Book.objects.filter(id=pk).all()[0]
    if picked_book.lending_status == "free":
        picked_book.lending_status = "lent"
    elif picked_book.lending_status == "lent":
        picked_book.lending_status = "free"
    picked_book.save()

    return redirect(request.META['HTTP_REFERER'])


class ChangeBookShelf(UpdateView):
    model = Book
    form_class = BookChangeShelfForm
    template_name = "manage_library/change_book_shelf.html"
    success_url = "/listallbooks/"


class ChangeBookShelf(UpdateView):
    model = Book
    form_class = BookChangeShelfForm
    template_name = "manage_library/change_book_shelf.html"
    success_url = "/listallbooks/"
