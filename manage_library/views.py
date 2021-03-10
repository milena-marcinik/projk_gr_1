from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView

from manage_library.models import Room, Bookcase, Shelf


# TODO decorator of log in
def main_manage_library(request):
    pass
    return render(request, template_name="manage_library/main_manage_library.html")


class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms_all'  # your own name for the list as a template variable
    queryset = Room.objects.all()
    template_name = 'manage_library/rooms_all.html'  # Specify your own template name/location


class RoomCreateView(CreateView):
    model = Room
    fields = ['name']
    success_url = '/room/'

    def form_valid(self, form):
        return super().form_valid(form)


class BookcaseListView(ListView):
    model = Bookcase
    context_object_name = 'bookcases_all'  # your own name for the list as a template variable
    queryset = Bookcase.objects.all()
    template_name = 'manage_library/bookcase_all.html'  # Specify your own template name/location


class BookcaseCreateView(CreateView):
    model = Bookcase
    fields = ['room', 'name']
    success_url = '/bookcase/'

    def form_valid(self, form):
        return super(BookcaseCreateView, self).form_valid(form)


class ShelfListView(ListView):
    model = Shelf
    context_object_name = 'shelves_all'  # your own name for the list as a template variable
    queryset = Shelf.objects.all()
    template_name = 'manage_library/shelf_all.html'  # Specify your own template name/location


class ShelfCreateView(CreateView):
    model = Shelf
    fields = ['room', 'bookcase', 'name']
    success_url = '/shelf/'

    def form_valid(self, form):
        form.instance.bookcase = Room.objects.filter(id=self.kwargs.get('pk'))
        return super(ShelfCreateView, self).form_valid(form)
