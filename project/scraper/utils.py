import requests
from bs4 import BeautifulSoup
from .models import Book, Language

def scrape_chitai_gorod(query):
    base_url = "https://www.chitai-gorod.ru/search?phrase="
    search_url = base_url + query
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_cards = soup.find_all('article', class_='product-card')
        for card in product_cards:
            title_tag = card.find('div', class_='product-title__head')
            title = title_tag.text.strip() if title_tag else 'Нет названия'
            author_tag = card.find('div', class_='product-title__author')
            author = author_tag.text.strip() if author_tag else 'Нет автора'
            price_tag = card.find('div', class_='product-price__value')
            price = price_tag.text.strip() if price_tag else 'Нет цены'
            Book.objects.create(title=title, author=author, price=price)

def scrape_tiobe_index():
    url = "https://www.tiobe.com/tiobe-index/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
  
        table = soup.find('table', {'class': 'table table-striped table-top20'})
        
        if table:

            for tr in table.find_all('tr')[1:]:
                cells = [td.text.strip() for td in tr.find_all('td')]

                if len(cells) >= 4:

                    ind = cells[0]
                    name = cells[1]
                    rating = cells[2]
                    change = cells[3]
         
                    Language.objects.create(
                        ind=ind,
                        name=name,
                        rating=rating,
                        change=change
                    )
