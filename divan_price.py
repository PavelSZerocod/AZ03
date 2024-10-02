import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.divan.ru/category/divany'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

prices = []
for price_tag in soup.find_all(class_='ui-LD-ZU KIkOH'):
    price_text = price_tag.get_text(strip=True)
    price_text = price_text.replace('₽', '').replace('руб.', '').replace(' ', '')
    try:
        price = int(price_text)
        prices.append(price)
    except ValueError:
        print(f"Не удалось преобразовать цену: {price_text}")

df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('sofa_prices.csv', index=False)

average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

plt.hist(df['Price'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (Руб.)')
plt.ylabel('Количество')
plt.show()