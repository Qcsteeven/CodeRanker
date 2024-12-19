import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table table-striped table-top20'})
    if table:
        headers = ["ind"] + [th.text.strip() for th in table.find_all('th')]
        rows = []
        for tr in table.find_all('tr'):
            cells = [td.text.strip() for td in tr.find_all('td')]
            if cells:
                rows.append(cells)
        rows = [row for row in rows if len(row) == len(headers)]
        df = pd.DataFrame(rows, columns=headers)
        print(df)
        df.to_csv('tiobe_index.csv', index=False)
    else:
        print("Таблица не найдена.")
else:
    print(f"Ошибка при запросе страницы: {response.status_code}")
