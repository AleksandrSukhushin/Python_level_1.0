# f(x) = -12x**4*sin(cos(x)) - 18x**3+5x**2 + 10x - 30

# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return -12*x ** 4*np.sin(np.cos(x)) - 18*x ** 3+5*x**2 + 10*x-30

x = np.linspace(-10, 10, 1000)
y = [function(x) for x in x]

plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции: -12x4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30')
plt.grid(True)
plt.show()
