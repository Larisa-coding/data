import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Используем правильный URL страницы каталога, а не главную страницу
url = "https://www.divan.ru/category/divany-i-kresla"

# Добавляем заголовки для обхода блокировки ботов
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

prices = []

# Ищем блоки с товарами
for item in soup.find_all('div', {"data-testid": "product-card"}):
    # Ищем элемент, содержащий цену
    price_tag = item.find('span', {"data-testid": "price"})
    if price_tag:
        # Очищаем текст от лишних символов
        price_text = price_tag.text.replace("руб.", "").replace(" ", "").strip()
        if price_text.isdigit():
            prices.append(int(price_text))  # Преобразуем в число

if not prices:
    print("Цены не найдены! Проверьте разметку сайта.")

df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('prices.csv', index=False)

if not df.empty:
    average_price = df['Price'].mean()
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")

    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='blue', alpha=0.7)
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(axis='y')
    plt.show()
else:
    print("Нет данных для построения графика.")
