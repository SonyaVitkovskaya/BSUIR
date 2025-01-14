import numpy as np
import matplotlib.pyplot as plt

#learning_rate
learning_rates =  [0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009, 0.001, 0.001001, 0.001005]
test_results = [
    [547, 521, 523, 498, 507],
    [236, 248, 226, 223, 231],
    [141, 126, 135, 130, 128],
    [85, 84, 81, 75, 79],
    [56, 58, 52, 57, 53],
    [37, 40, 38, 38, 38],
    [30, 30, 29, 28, 29],
    [24, 19, 20, 22, 21],
    [16, 15, 16, 17, 16],
    [14, 13, 14, 11, 13],
    [11, 13, 11, 12, 10],
    [12, 8, 11, 11, 12]
]


averages = [np.mean(results) for results in test_results]
plt.figure(figsize=(10, 7))
plt.axvline(x=0.00101, color="gray", linestyle="--")
for i, results in enumerate(test_results):
    plt.scatter([learning_rates[i]] * len(results), results, alpha=0.6)

plt.plot(learning_rates, averages, color='green', linestyle='-',  linewidth=0.7)
plt.xlabel('Коэффициент обучения')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()




#max_error
max_error =[1100, 1200, 1350, 1500, 1700, 1900, 2300, 2500, 3000]
test_results_max_error = [
    [593, 624, 611, 598, 527],
    [255, 265, 256, 239, 217],
    [124, 117, 120, 114, 109],
    [87, 75, 76, 82, 77],
    [60, 55, 53, 59, 57],
    [44, 42, 39, 40, 45],
    [26, 28, 24, 25, 29],
    [22, 24, 20, 21, 25],
    [16, 17, 14, 16, 17],
]

averages_max_error = [np.mean(results) for results in test_results_max_error]
plt.figure(figsize=(8, 7))
for i, results in enumerate(test_results_max_error):
    plt.scatter([max_error[i]] * len(results), results, alpha=0.6)
plt.plot(max_error, averages_max_error, color='green', linestyle='-', linewidth=0.7)
plt.xlabel('Максимально допустимая ошибка')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()

#Z
Z_values = [
    26.93998355713894, 20.206372045220967, 13.471837741537618,
    10.104224483502929, 6.7363804563831975,
    5.052371897003649, 3.3683056364570843, 2.526250867319405
    ]

test_results = [
    [99, 97, 100, 102, 95],
    [87, 85, 88, 91, 90],
    [72, 74, 70, 69, 71],
    [66, 65, 64, 68, 67],
    [72, 70, 71, 73, 74],
    [69, 71, 68, 70, 69],
    [79, 81, 78, 80, 77],
    [80, 79, 81, 78, 82]
]

averages = [np.mean(results) for results in test_results]
plt.figure(figsize=(8, 7))

for i, results in enumerate(test_results):
    plt.scatter([Z_values[i]] * len(results), results, alpha=0.6)

plt.plot(Z_values, averages, color='green', linestyle='-', linewidth=0.7)
plt.xlabel('Коэффициент сжатия Z')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.xlim(0, max(Z_values) + 1)
plt.ylim(0, max(test_results[0]) + 10)
plt.show()