from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    id = models.CharField(max_length=100, unique=True)


class Book(models.Model):
    id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=180, required=True)
    author = models.CharField(max_length=100, required=True)
    isbn_number = models.CharField(max_length=13)
    note = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.SET_NULL)
    cover = models.ImageField()
    shelf = models.ForegnKey(Shelf, models.SET_NULL)
    lending_status = models.BooleanField()

class Shelf(models.Model):
    bookcase = models.ForeignKey(Shelf, max_length=20)
    id = models.CharField(max_length=100, unique=True)




