from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Room(models.Model):
    name = models.CharField(max_length=20)


class Bookcase(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, max_length=130, on_delete=models.DO_NOTHING)


class Shelf(models.Model):
    bookcase = models.ForeignKey(Bookcase, max_length=20, on_delete=models.DO_NOTHING)


class Book(models.Model):
    title = models.CharField(max_length=180, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField( max_length=13,validators=[
            RegexValidator(regex='^[0-9]{10}$', message="Wrong ISBN length"),
            RegexValidator(regex='^[0-9]{13}$', message="Wrong ISBN length"),
    ])
    note = models.TextField()
    cover = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True)
    lending_status = models.CharField(max_length=4, choices=[
        ("lent", "lent",),
        ("free", "free",),
    ], default="free")
