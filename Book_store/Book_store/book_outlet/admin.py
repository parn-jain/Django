from django.contrib import admin

# Register your models here.
from .models import Book, Address ,Author, Country

# class AddressAdmin(admin.ModelAdmin):
#     list_display = ("street", "postal_code", "city")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","address")


class BookAdmin(admin.ModelAdmin):
    # read_only = ("slug",)
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author","rating",)
    list_display = ("title","author")


admin.site.register(Book,BookAdmin)
admin.site.register(Address)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Country)


