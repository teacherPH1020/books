from django.shortcuts import render
from .forms import AuthorForm, BookForm, ShelfForm

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
    print(request.POST, type(request.POST), bool(request.POST)) #TODO delete
    if request.method == 'GET':
        form = AuthorForm()
    elif request.method == 'POST':
        if request.POST.get('name', False):
            form = AuthorForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
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