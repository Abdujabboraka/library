from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Books, Readers, Borrowed_books
# Create your views here.

def home(request):
    book = Books.objects.all()
    reader = Readers.objects.all()
    borrow = Borrowed_books.objects.all()
    context = {
        'book': book,
        'reader': reader,
        'borrow': borrow,    }
    return render(request, 'home.html', context)

