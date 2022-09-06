from django.contrib import admin
from .models import Book, Author, Shelf

# Register your models here.
admin.site.register(Book)
admin.site.register(Shelf)
admin.site.register(Author)