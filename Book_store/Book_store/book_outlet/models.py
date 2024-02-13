from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify


# Create your models here.

class Country(models.Model):
    name = models.CharField( max_length=80)
    code = models.CharField(max_length = 2)
    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length = 100)
    postal_code = models.CharField( max_length=50)
    city = models.CharField( max_length=50)

    def __str__(self):
        return f"{self.street},{self.postal_code},{self.city}"
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address Entries"



class Author(models.Model):
    name = models.CharField(max_length = 100)
    address = models.OneToOneField( Address , on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 100)
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null = True, max_length = 50)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, related_name = "books") 
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default = '', null =False,blank = True , db_index = True)
    published_countries = models.ManyToManyField(Country,null = False)

    def save(self,*args,**kwargs):
        # self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"{self.title} ({self.author,self.rating})"