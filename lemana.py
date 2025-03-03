from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup  # Импорт BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# Настройка Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме
driver = webdriver.Chrome(options=options)

# URL сайта со строительными материалами
url = "https://irkutsk.lemanapro.ru/catalogue/dushevye-kabiny-i-shirmy/"

# Открываем страницу
driver.get(url)
time.sleep(5)  # Ждем загрузки страницы

# Получаем HTML-код страницы
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")  # Использование BeautifulSoup

# Список для хранения цен
prices = []

# Ищем блоки с товарами
item_blocks = soup.find_all('div', class_='product-item')

for item in item_blocks:
    # Ищем цену товара
    price_tag = item.find('span', class_='price_value')

    if price_tag:
        text = price_tag.get_text(strip=True)  # Получаем текст цены
        if "₽" in text:
            prices.append(text)

# Уникальные значения цен
unique_prices = set(prices)

# Обрабатываем каждый найденный элемент
cleaned_prices = []
for price_text in unique_prices:
    # Очищаем текст, убираем лишние символы и получаем только цену
    price_clean = price_text.split("₽")[0].strip()
    price_clean = price_clean.replace("\u202f", "").replace(" ", "")

    try:
        price_val = int(price_clean)
        cleaned_prices.append(price_val)
    except ValueError:
        continue

# Удаляем дубликаты для окончательной обработки
cleaned_prices = list(set(cleaned_prices))

if not cleaned_prices:
    print("Цены не найдены!")
else:
    df = pd.DataFrame(cleaned_prices, columns=["Price"])
    df.to_csv("prices.csv", index=False)

    average_price = df["Price"].mean()
    print(f"Средняя стоимость: {average_price:.2f} ₽")

    plt.figure(figsize=(10, 6))
    plt.hist(df["Price"], bins=20, color="blue", alpha=0.7)
    plt.title("Гистограмма цен на строительные материалы")
    plt.xlabel("Цена (₽)")
    plt.ylabel("Количество товаров")
    plt.grid(axis="y")
    plt.show()

# Закрываем браузер
driver.quit()