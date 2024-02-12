from django.shortcuts import render
from django.db.models import Avg
from .models import Book

# Create your views here.
def index(request):

    books = Book.objects.all()
    tb = books.count()
    avgr = books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
        "books": books,
        "total_books": tb,
        "average_rating": avgr
    })

def book_details(request,slug):
    # books = Book.objects.all()
    book = Book.objects.get(slug = slug)   #2nd slug is the functino mparamiter nad 1st slug id the module attribute
    # identify = next(book for book in books if book['title']==slug)
    return render(request,"book_outlet/book_detail.html",{
        # "books":identify
        "book":book

    })


