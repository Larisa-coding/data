import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
