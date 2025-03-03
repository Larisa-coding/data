import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL вакансий
url = "https://irkutsk.hh.ru/vacancies/programmist"

# Заголовки для обхода блокировок
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

salaries = []

# Находим все <span> с нужным классом (который встречается у зарплат) и содержащие ₽
salary_spans = soup.find_all("span",
                             class_="magritte-text___pbpft_3-0-27 magritte-text_style-primary___AQ7MW_3-0-27 magritte-text_typography-label-1-regular___pi3R-_3-0-27")
unique_salaries = set()

for span in salary_spans:
    text = span.get_text(strip=True)
    if "₽" in text:
        unique_salaries.add(text)

# Обрабатываем каждый найденный элемент
for salary_text in unique_salaries:
    # Отсекаем часть после символа ₽ (например, "за месяц, до вычета налогов")
    salary_clean = salary_text.split("₽")[0].strip()
    # Убираем неразрывные пробелы (например, U+202F)
    salary_clean = salary_clean.replace("\u202f", "").replace(" ", "")

    # Если в строке присутствует диапазон зарплат (разделитель –)
    if "–" in salary_clean:
        try:
            low, high = salary_clean.split("–")
            low = int(low)
            high = int(high)
            average = (low + high) / 2
            salaries.append(average)
        except ValueError:
            continue
    else:
        try:
            salary_val = int(salary_clean)
            salaries.append(salary_val)
        except ValueError:
            continue

if not salaries:
    print("Заработные платы не найдены!")
else:
    df = pd.DataFrame(salaries, columns=["Salary"])
    df.to_csv("salaries.csv", index=False)

    average_salary = df["Salary"].mean()
    print(f"Средняя зарплата: {average_salary:.2f} ₽")

    plt.figure(figsize=(10, 6))
    plt.hist(df["Salary"], bins=20, color="blue", alpha=0.7)
    plt.title("Гистограмма зарплат")
    plt.xlabel("Зарплата (₽)")
    plt.ylabel("Количество вакансий")
    plt.grid(axis="y")
    plt.show()
