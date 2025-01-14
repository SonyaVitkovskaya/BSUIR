import numpy as np
import matplotlib.pyplot as plt

#iterations
number =  [i for i in range(1, 12)]
iterations = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 2]

plt.figure(figsize=(10, 7))
plt.scatter(number, iterations, alpha=0.6)

plt.xlabel('Количество подаваемых образов')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()


#detected
number =  [i for i in range(1, 11)]
test_results = [1, 2, 3, 4, 4, 5, 6, 5, 4, 4]

plt.figure(figsize=(10, 7))
plt.scatter(number, test_results, alpha=0.6)

plt.xlabel('Количество подаваемых образов')
plt.ylabel('Число итераций')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.3)
plt.show()
