import os
import json

from django.contrib.auth.models import User
from manage_library.models import Category, Room, Bookcase, Shelf, Book

current_wkd = os.getcwd() + "\manage_library\\auxiliaries\\"

add_categories = False
add_rooms = False
add_bookcases = False
add_shelves = False
add_books = False
add_users = True

if add_categories:
    with open(current_wkd+"categories.json") as h:
        categories = json.load(h)
    for category in categories:
        Category(name=category["name"]).save()

if add_rooms:
    with open(current_wkd+"rooms.json") as h:
        rooms = json.load(h)
    for room in rooms:
        Room(name=room["name"]).save()

if add_bookcases:
    with open(current_wkd+"bookcases.json") as h:
        bookcases = json.load(h)
    for bookcase in bookcases:

        Bookcase(name=bookcase["name"],
                 room=Room.objects.filter(name=bookcase["room"]).all()[0]
                ).save()

if add_shelves:
    with open(current_wkd+"shelves.json") as h:
        shelves = json.load(h)
    for shelf in shelves:
        Shelf(name=shelf["name"],
              bookcase=Bookcase.objects.filter(name=shelf["bookcase"]).all()[0]
             ).save()

if add_books:
    with open(current_wkd+"books.json", encoding="utf8") as h:
        books = json.load(h)
    for book in books:
        Book(
            title=book["title"],
            author=book["author"],
            isbn_number=book.get("isbn_number", ""),
            note=book.get("note", ""),
            #cover=
            category=Category.objects.filter(name=book["category"]).all()[0],
            shelf=Shelf.objects.filter(name=book["shelf"])
                .filter(bookcase__name=book["bookcase"])
                .filter(bookcase__room__name=book["room"])
                .all()[0]
            #lending_status=
        ).save()

if add_users:
    with open(current_wkd+"users.json", encoding="utf8") as h:
        users = json.load(h)
    for user in users:
        User(
            username=user["username"],
            password=user["password"],
            is_superuser=user["is_superuser"],
        ).save()