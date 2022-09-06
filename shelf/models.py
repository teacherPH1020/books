from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)
    pic = models.ImageField()
    bio = models.TextField()

class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    pic = models.FileField(upload_to='book_pics/')

class Shelf(models.Model):
    pass
