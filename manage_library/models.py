from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Room(models.Model):
    name = models.CharField(max_length=20)


class Bookcase(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, max_length=130)


class Shelf(models.Model):
    bookcase = models.ForeignKey(Bookcase, max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=180, required=True)
    author = models.CharField(max_length=100, required=True)
    isbn_number = models.CharField(max_length=13)
    note = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.SET_NULL)
    cover = models.ImageField()
    shelf = models.ForeignKey(Shelf, models.SET_NULL)
    lending_status = models.BooleanField()
