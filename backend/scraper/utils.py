import os
import re
import django
import requests
from time import sleep
from bs4 import BeautifulSoup
from scraper.models import Language, Book

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def scrape_chitai_gorod(query):
    dct_in = {"C++": "C%2B%2B", "C": "Язык С", "Delphi/Object Pascal" : "Pascal",
              "Assembly language": "Assembler", "C#": "Язык%20C", "R": "Искусство программирования на R"}
    dct_to = {"C%2B%2B": "C++",
              "Язык%20C": "C#", "Assembly language": "Assembler", "Искусство программирования на R" : "R"}
    correct = {"Pascal" : "Delphi/Object Pascal", "Assembler" : "Assembly language", "Язык С" : "C"}
    page = 1
    count = 0
    while True:
        
        if query in dct_in:
            query = dct_in[query]
        search_url = f"https://www.chitai-gorod.ru/search?phrase={query}&page={page}&filters%5Bcategories%5D=110299"
        response = requests.get(search_url)
        if query in dct_to:
            query = dct_to[query]
        print(query)
            
        if response.status_code != 200 or page > 15:
            break
        
        if response.status_code == 200 and count < 5:
            soup = BeautifulSoup(response.text, 'html.parser')
            product_cards = soup.find_all('article', class_='product-card')
            for card in product_cards:
                title_tag = card.find('div', class_='product-title__head')
                title = title_tag.text.strip() if title_tag else 'Нет названия'
                author_tag = card.find('div', class_='product-title__author')
                author = author_tag.text.strip() if author_tag else 'Нет автора'
                price_tag = card.find('div', class_='product-price__value')
                price = price_tag.text.strip() if price_tag else 'Нет цены'
                ref_tag = card.find('a', class_='product-card__picture')
                ref = "https://www.chitai-gorod.ru" + ref_tag['href'] if ref_tag and ref_tag.has_attr('href') else 'Нет ссылки'
                print(ref)
                if re.search(r'\b' + re.escape(query) + r'[\s\:\.\-\(\)]', title, re.IGNORECASE) and ref and not Book.objects.filter(lang=query, title=title, ref=ref).exists():
                    if query in correct:
                        query = correct[query]
                    Book.objects.create(lang=query, title=title, author=author, ref=ref)
                    count += 1
                    if count == 5:
                        break
            page += 1
        else:
            break
        
       

def scrape_tiobe_index():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'table table-striped table-top20'})
        
        if table:
            for tr in table.find_all('tr')[1:]:
                
                cells = [td.text.strip() for td in tr.find_all('td')]
                cells = [cells[0]] + cells[4:]
                if len(cells) >= 4:
                    ind = cells[0]
                    name = cells[1]
                    rating = cells[2]
                    change = cells[3]
                    if tr:
                        img_tag = tr.find_all('img')[-1]
                    logo_url = ""
                    if img_tag:
                        logo_url = img_tag['src']
                        if not logo_url.startswith("http"):
                            logo_url = "https://www.tiobe.com" + logo_url
                    print(logo_url)
                    Language.objects.create(
                        ind=ind,
                        name=name,
                        rating=rating,
                        change=change,
                        logo=logo_url
                    )
