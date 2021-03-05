from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"name: {self.name}"


class Room(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __repr__(self):
        return f"name: {self.name}"


class Bookcase(models.Model):
    name = models.CharField(max_length=20, unique=True)
    room = models.ForeignKey(Room, max_length=130, on_delete=models.CASCADE, null=False)

    def __repr__(self):
        return f"name: {self.name} room.name: {self.room.name}"


class Shelf(models.Model):
    number = models.TextField(max_length=3)
    bookcase = models.ForeignKey(Bookcase, max_length=20, on_delete=models.CASCADE, null=False)

    def __repr__(self):
        return f"number: {self.number} bookcase name: {self.bookcase.name}"


class Book(models.Model):
    title = models.CharField(max_length=180, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=13, validators=[
        RegexValidator(regex='^[0-9]{10}$', message="Wrong ISBN length"),
        RegexValidator(regex='^[0-9]{13}$', message="Wrong ISBN length"),
    ])
    note = models.TextField(default="no note")
    cover = models.ImageField(upload_to="covers", default="covers/default_cover.jpg")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)
    bookcase = models.ForeignKey(Bookcase, on_delete=models.CASCADE, null=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=False)
    lending_status = models.CharField(max_length=4, choices=[
        ("lent", "lent",),
        ("free", "free",),
    ], default="free")

    def __repr__(self):
        return f"title: {self.title}, author: {self.author}"
