from django.shortcuts import render
from .models import Book, Language
from .utils import scrape_chitai_gorod, scrape_tiobe_index

def home(request):
    if not Book.objects.exists():
        scrape_chitai_gorod('Python') 
    if not Language.objects.exists():  
        scrape_tiobe_index()

    books = Book.objects.all()
    languages = Language.objects.all()

    return render(request, 'home.html', {'books': books, 'languages': languages})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

def languages_list(request):
    languages = Language.objects.all()
    return render(request, 'languages_list.html', {'languages': languages})
