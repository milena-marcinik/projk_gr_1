from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"id: {self.id} name: {self.name}"

class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"id: {self.id} name: {self.name}"

class Bookcase(models.Model):
    name = models.CharField(max_length=20, unique=True)
    room = models.ForeignKey(Room, max_length=130, on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"id: {self.id} name: {self.name} room.name: {self.room.name}"

class Shelf(models.Model):
    bookcase = models.ForeignKey(Bookcase, max_length=20, on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"id: {self.id} bookcase.id: {self.bookcase.id}"

class Book(models.Model):
    title = models.CharField(max_length=180, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField( max_length=13,validators=[
            RegexValidator(regex='^[0-9]{10}$', message="Wrong ISBN length"),
            RegexValidator(regex='^[0-9]{13}$', message="Wrong ISBN length"),
    ])
    note = models.TextField()
    cover = models.ImageField(upload_to = "covers", default="covers/default_cover.jpg")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True)
    lending_status = models.CharField(max_length=4, choices=[
        ("lent", "lent",),
        ("free", "free",),
    ], default="free")

    def __repr__(self):
        return f"id: {self.id} title: {self.title}"