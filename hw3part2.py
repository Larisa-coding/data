import numpy as np
import matplotlib.pyplot as plt

random_array_x = np.random.rand(5)
random_array_y = np.random.rand(5)

print("Случайные данные по оси X:", random_array_x)
print("Случайные данные по оси Y:", random_array_y)

plt.scatter(random_array_x, random_array_y, color='blue', marker='o')
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("Случайные данные по оси X")
plt.ylabel("Случайные данные по оси Y")

plt.grid()
plt.show()
