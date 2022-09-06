from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=256)
    pic = models.ImageField(upload_to='author_pics/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    author = models.ManyToManyField(Author)
    year = models.IntegerField()
    pic = models.FileField(upload_to='book_pics/')

    def __str__(self):
        return self.title

class Shelf(models.Model):
    location = models.SlugField(default='')
    load = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.location


