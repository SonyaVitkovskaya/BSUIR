import numpy as np
import matplotlib.pyplot as plt

# Таблица 1: Зависимость количества итераций от порогового значения ошибки
max_error = np.array([1100, 1200, 1350, 1500, 1700, 1900, 2300, 2500, 3000])
iterations_error = np.array([
    [593, 624, 611, 598, 527],
    [255, 265, 256, 239, 217],
    [124, 117, 120, 114, 109],
    [87, 75, 76, 82, 77],
    [60, 55, 53, 59, 57],
    [44, 42, 39, 40, 45],
    [26, 28, 24, 25, 29],
    [22, 24, 20, 21, 25],
    [16, 17, 14, 16, 17]
])
avg_error = iterations_error.mean(axis=1)

# Таблица 2: Зависимость количества итераций от коэффициента обучения
learning_rate = np.array([0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001])
iterations_lr = np.array([
    [547, 521, 523, 498, 507],
    [236, 248, 226, 223, 231],
    [141, 126, 135, 130, 128],
    [85, 84, 81, 75, 79],
    [56, 58, 52, 57, 53],
    [37, 40, 38, 38, 38],
    [30, 30, 29, 28, 29],
    [24, 19, 20, 22, 21],
    [16, 15, 16, 17, 16],
    [14, 13, 14, 11, 13]
])
avg_lr = iterations_lr.mean(axis=1)

# Таблица 3: Зависимость количества итераций от коэффициента сжатия
p = np.array([16, 24, 32, 48, 64, 96, 120])
Z = np.array([10.104224483502929, 6.7363804563831975, 5.052371897003649, 
              3.3683056364570843, 2.526250867319405, 1.6841816717778273, 
              1.347349954085059])
iterations_compression = np.array([
    [66, 67, 67, 66, 69],
    [65, 67, 63, 62, 66],
    [71, 72, 74, 73, 71],
    [75, 77, 76, 74, 74],
    [83, 80, 83, 80, 81],
    [90, 88, 89, 87, 88],
    [92, 91, 88, 92, 93]
])
avg_compression = iterations_compression.mean(axis=1)
# Построение графиков в отдельных окнах

# График 1: Зависимость количества итераций от порогового значения ошибки
plt.figure(figsize=(8, 6))
for i, row in enumerate(iterations_error):
    plt.scatter([max_error[i]] * len(row), row, color='blue', alpha=0.5)
plt.plot(max_error, avg_error, color='red', marker='o')
plt.xlabel("Max Error")
plt.ylabel("Iterations")
plt.legend()
plt.grid()
plt.show()

# График 2: Зависимость количества итераций от коэффициента обучения
plt.figure(figsize=(8, 6))
for i, row in enumerate(iterations_lr):
    plt.scatter([learning_rate[i]] * len(row), row, color='blue', alpha=0.5)
plt.plot(learning_rate, avg_lr, color='red', marker='o')
plt.xlabel("Learning Rate")
plt.ylabel("Iterations")
plt.xscale('log')
plt.legend()
plt.grid()
plt.show()

# График 3: Зависимость количества итераций от коэффициента сжатия
plt.figure(figsize=(8, 6))
for i, row in enumerate(iterations_compression):
    plt.scatter([Z[i]] * len(row), row, color='blue', alpha=0.5)
plt.plot(Z, avg_compression, color='red', marker='o')
plt.xlabel("Z")
plt.ylabel("Iterations")
plt.legend()
plt.grid()
plt.show()
