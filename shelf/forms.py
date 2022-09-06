from django import forms

from .models import Book, Author, Shelf

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        #fields = '__all__'
        exclude = ['pic'] #TODO fix pic

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = '__all__'
        exclude = ['pic'] # TODO fix pic

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = '__all__'
