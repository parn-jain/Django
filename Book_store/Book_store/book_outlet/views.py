from django.shortcuts import render

from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books": books
    })

def book_details(request,id):
    # books = Book.objects.all()
    book = Book.objects.get(pk = id)
    # identify = next(book for book in books if book['title']==slug)
    return render(request,"book_outlet/book_detail.html",{
        # "books":identify
        "book":book

    })


