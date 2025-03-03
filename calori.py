import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL сайта с калориями
url = "https://calorizator.ru/product/beef"

# Заголовки для обхода блокировок
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

# Получаем содержимое страницы
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Список для хранения продуктов и их калорийности
products = []

# Ищем блоки с продуктами
item_blocks = soup.find_all('tr', class_='odd') + soup.find_all('tr', class_='even')

for item in item_blocks:
    # Ищем название продукта
    title = item.find('td', class_='views-field-title')
    # Ищем количество калорий
    calorie = item.find('td', class_='views-field-field-kcal-value')

    if title and calorie:
        title_text = title.get_text(strip=True)
        calorie_text = calorie.get_text(strip=True)

        # Убираем лишние символы и пробелы из текста с калориями
        calorie_text = ''.join(filter(str.isdigit, calorie_text))

        # Проверяем, что текст с калориями является числом
        if calorie_text:
            products.append({'name': title_text, 'calories': int(calorie_text)})

# Проверяем, найдены ли продукты
if not products:
    print("Продукты не найдены!")
else:
    # Создаем DataFrame из списка продуктов
    df = pd.DataFrame(products)

    # Упорядочиваем продукты по количеству калорий
    df_sorted = df.sort_values(by='calories')

    # Находим 5 высококалорийных и 5 низкокалорийных продуктов
    high_calories = df_sorted.tail(5)
    low_calories = df_sorted.head(5)

    # Сохраняем результаты в файл
    with pd.ExcelWriter('calories.xlsx') as writer:
        high_calories.to_excel(writer, sheet_name='High Calorie Products', index=False)
        low_calories.to_excel(writer, sheet_name='Low Calorie Products', index=False)

    print("Данные о продуктах с высоким и низким содержанием калорий сохранены в 'calories.xlsx'.")