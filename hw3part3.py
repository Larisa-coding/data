import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.divan.ru/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

prices = []
for item in soup.find_all('div', class_='m8TzZ', itemprop='offers'):
    price = item.find('span', itemprop='price')
    if price:
        prices.append(float(price['content']))

df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('prices.csv', index=False)

average_price = df['Price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} ₽")

plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y')
plt.show()
