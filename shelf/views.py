from django.shortcuts import render
from .forms import AuthorForm, BookForm, ShelfForm
from .models import Author, Book, Shelf

# Create your views here.
def add_shelf_view(request):
    context = {}
    form = ShelfForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    else:
        context['alert'] = 'Form is invalid'
    context['form'] = form
    return render(request, 'add_form.html', context=context)

def add_book_view(request):
    context = {}
    context['alert'] = ''
    if request.method == 'GET':
        context['form_purpose'] = 'Enter Author info'
        sample = Author.objects.get(pk=1)
        form = AuthorForm(instance=sample)
    elif request.method == 'POST':
        if request.POST.get('name', False):
            form = AuthorForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                context['form_purpose'] = 'Enter Book info'
                form = BookForm()
            else:
                context['alert'] = 'Form is invalid'
        elif request.POST.get('title', False):
            form = BookForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                form = AuthorForm()
            else:
                context['alert'] = 'Form is invalid'
    context['form'] = form
    return render(request, 'add_form.html', context=context)