import requests
from bs4 import BeautifulSoup


def scrape_chitai_gorod(query):
    base_url = "https://www.chitai-gorod.ru/search?phrase="
    search_url = base_url + query
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_cards = soup.find_all('article', class_='product-card')
        books = []
        for card in product_cards:
            title_tag = card.find('div', class_='product-title__head')
            title = title_tag.text.strip() if title_tag else 'Нет названия'
            author_tag = card.find('div', class_='product-title__author')
            author = author_tag.text.strip() if author_tag else 'Нет автора'
            price_tag = card.find('div', class_='product-price__value')
            price = price_tag.text.strip() if price_tag else 'Нет цены'
            books.append({'Название': title, 'Автор': author, 'Цена': price})
            print(books[-1])


scrape_chitai_gorod("Python")
