from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Room(models.Model):
    name = models.CharField(max_length=20)


class Bookcase(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, max_length=130)  # TODO trzeba jeszcze on_delete


class Shelf(models.Model):
    bookcase = models.ForeignKey(Bookcase, max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=180, required=True, blank=False)
    author = models.CharField(max_length=100, required=True, blank=False)
    isbn_number = models.CharField(validator=[
        RegexValidator(regex='^[0-9]{10}$', message="Wrong ISBN length"),
        RegexValidator(regex='^[0-9]{13}$', message="Wrong ISBN length"),
    ])
    note = models.TextField()
    cover = models.ImageField()
    category = models.ForeignKey(Category, models.SET_NULL)  # TODO trzeba jeszcze on_delete
    shelf = models.ForeignKey(Shelf, models.SET_NULL)  # TODO trzeba jeszcze on_delete
    lending_status = models.CharField(choices=[
        (lent, "lent",),
        (free, "free"),
    ], default=free)
