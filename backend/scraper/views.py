from django.shortcuts import render
from scraper.models import Book, Language

def home(request):
    languages = Language.objects.all()
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'languages': languages})

