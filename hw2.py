import pandas as pd
import numpy as np

data = {
    'Ученик': ['Аня', 'Боб', 'Чарли', 'Лиза', 'Настя', 'Саша', 'Сергей', 'Максим', 'Иван', 'Станислав'],
    'Математика': [5, 4, 3, 4, 5, 2, 4, 3, 4, 5],
    'Физика': [4, 4, 3, 5, 3, 2, 5, 4, 4, 4],
    'Химию': [5, 5, 4, 3, 4, 3, 5, 2, 4, 5],
    'История': [3, 4, 4, 5, 4, 2, 3, 5, 5, 4],
    'Литература': [4, 5, 4, 5, 5, 3, 4, 3, 4, 4]
}

df = pd.DataFrame(data)

print("Первые строки DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математике: {Q1_math}")
print(f"Q3 для математике: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"\nIQR для математике: {IQR_math}")

std_devs = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_devs)
