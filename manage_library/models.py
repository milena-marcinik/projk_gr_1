from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"name: {self.name}"

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __repr__(self):
        return f"name: {self.name}"

    def __str__(self):
        return self.name


class Bookcase(models.Model):
    name = models.CharField(max_length=20, unique=True)
    room = models.ForeignKey(Room, max_length=130, on_delete=models.CASCADE, null=False)

    def __repr__(self):
        return f"name: {self.name} room.name: {self.room.name}"

    def __str__(self):
        return self.name


class Shelf(models.Model):
    name = models.CharField(max_length=20, default="")
    bookcase = models.ForeignKey(Bookcase, max_length=20, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = [["name", "bookcase"]]

    def __repr__(self):
        return f"id: {self.id} name: {self.name} bookcase: {self.bookcase.name} room: {self.bookcase.room.name}"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=180, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=13, validators=[
        RegexValidator(regex='^[0-9]{10}$', message="Wrong ISBN length"),
        RegexValidator(regex='^[0-9]{13}$', message="Wrong ISBN length"),
    ])
    note = models.TextField(default="no note")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=True)
    lending_status = models.CharField(max_length=4, choices=[
        ("lent", "lent",),
        ("free", "free",),
    ], default="free")

    def __repr__(self):
        return f"title: {self.title}, author: {self.author}"
