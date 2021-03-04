from manage_library.models import Category, Room, Bookcase, Shelf, Book

## Kategorie
# Category(name="Kryminaly").save()
# Category(name="Słowniki").save()
# Category(name="Podręczniki szkolne").save()

## Pokoje
# Room(name="Magazynek").save()
# Room(name="Schowek pod schodami").save()
# Room(name="Piwnica").save()

## Regaly
# Bookcase(name="Szafa pancerna", room=Room.objects.filter(name="Magazynek").first()).save()
#
# Bookcase(name="Witryna", room=Room.objects.filter(name="Schowek pod schodami").first()).save()
# Bookcase(name="Szafa", room=Room.objects.filter(name="Schowek pod schodami").first()).save()
#
# Bookcase(name="Polki przy oknie", room=Room.objects.filter(name="Piwnica").first()).save()

## Polki
# for _ in range(0, 4):
#     Shelf(bookcase=Bookcase.objects.filter(name="Szafa pancerna").first()).save()
#     Shelf(bookcase=Bookcase.objects.filter(name="Polki przy oknie").first()).save()

## Ksiazki

Book(
    title = "Zbrodnia Ikara",
    author = "Minos Dostojewski",
    isbn_number = "0123456789",
    note = "Rogi lekko zadarte. Odbite dno szklanki z kawy na okladce",
    # Ccover defaultowy
    category = Category.objects.filter(name="Kryminaly").first(),
    shelf = Shelf.objects.filter(bookcase__name="Szafa pancerna").first(),
    # lending_status defaultowy
).save()






