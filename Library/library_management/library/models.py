from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ManyToManyField('Author')
    genre = models.ManyToManyField('Genre')
    qty = models.IntegerField(default = 0)
    available_qty = models.IntegerField(default = 0)
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

class Authors:
    name = models.CharField(max_length = 100)
    biography = models.TextField()
    dob = models.DateField()
    dod = models.DateField()

class Genre:
    name = models.CharField(max_length = 100)
    pass

class Borrower:
    name = models.CharField(max_length = 80)
    email = models.EmailField()
    phone = models.PhoneNumberField()
    borrowed_books = models.ManyToManyField("BorrowedBooks")
    status = models.BooleanField(default = True)
    fine = models.IntegerField()
    # name
    # email
    # phonenumber
    # borrowed_books many to many relation with Borrowed Books
    # status
    # fine

    pass

class BorrowedBooks:
    name = models.ForeignKey("Borrowers", on_delete=models.CASCADE)
    books = models.ForeignKey("Books",on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()


    # borrowers
    # books foriegn key with books , 
    # borrow date
    # return date
    pass




# Project planing 
