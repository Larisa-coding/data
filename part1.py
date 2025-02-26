import pandas as pd
import numpy as np

data = {
    'Name': ['Аня', 'Боб', 'Чарли', 'Лиза', 'Настя', 'Саша', 'Сергей', 'Максим', 'Иван', 'Станислав', 'Вика', 'Мария'],
    'City': ['Томск', 'Москва', 'Москва', 'Томск', None, 'Томск', 'Москва', 'Москва', 'Москва', 'Москва', None, 'Томск'],
    'Salary': [200000, 350000, 270000, 70000, 35000, 23000, 250000, None, 67000, 120000, 47000, 72000]
}

df = pd.DataFrame(data)
df = df.dropna(subset=['Salary'])
df['Salary'] = pd.to_numeric(df['Salary'])
average_salary = df.groupby('City')['Salary'].mean()
print(average_salary)
