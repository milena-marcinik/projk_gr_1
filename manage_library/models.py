from PIL import Image
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"name: {self.name}"

    # def __str__(self):
    #     return self.name


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
        return f"room: {self.room}, bookcase: {self.name}"


class Shelf(models.Model):
    name = models.CharField(max_length=20, default="")
    bookcase = models.ForeignKey(Bookcase, max_length=20, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = [["name", "bookcase"]]

    def __repr__(self):
        return f"id: {self.id} name: {self.name} bookcase: {self.bookcase.name} room: {self.bookcase.room.name}"

    def __str__(self):
        return f"id:{self.id} : {self.name} : {self.bookcase.name} : {self.bookcase.room.name}"


class Book(models.Model):
    title = models.CharField(max_length=180, blank=False)
    author = models.CharField(max_length=100, blank=False)
    isbn_number = models.CharField(max_length=13, validators=[
        RegexValidator(regex='^[0-9]{10}$|^[0-9]{13}$', message="Wrong ISBN length"),
    ], blank=True)
    note = models.TextField(default="no note")
    cover = models.ImageField(upload_to="covers", default="covers/default_cover.jpg")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True, blank=True)
    lending_status = models.CharField(max_length=4, choices=[
        ("lent", "lent",),
        ("free", "free",),
    ], default="free")
    date_added = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f"title: {self.title}, author: {self.author}"

    def __str__(self):
        return self.title

    def save(self):

        this_book = Book.objects.get(id=self.id)
        if not this_book.cover.url.endswith("default_cover.jpg") and self.cover.url != this_book.cover.url:
            this_book.cover.delete(save=False)

        super().save()

        img = Image.open(self.cover.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover.path)
