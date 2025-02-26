import pandas as pd

file_path = 'heart_attack_prediction_india.csv'
data = pd.read_csv(file_path)

print("Первые 5 строк данных:")
print(data.head())

print("\nИнформация о данных:")
print(data.info())

print("\nСтатистическое описание:")
print(data.describe())
