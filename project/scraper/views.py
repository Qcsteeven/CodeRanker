from django.shortcuts import render
from scraper.models import Book, Language
from .utils import scrape_chitai_gorod, scrape_tiobe_index

def home(request):
    Language.objects.all().delete()
    Book.objects.all().delete()
    scrape_tiobe_index()
    languages = Language.objects.all()
    for language in languages:
        scrape_chitai_gorod(language.name)
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books, 'languages': languages})

