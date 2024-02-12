# myapp/utils.py

from book_outlet.models import Book

def generate_slugs_for_books():
    books = Book.objects.all()
    for book in books:
        book.save()
