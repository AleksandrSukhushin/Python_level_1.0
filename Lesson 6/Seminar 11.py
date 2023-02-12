# Дана функция: f(x) = 5*x**2 + 10*x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, solve, N, diff, simplify

x = symbols('x')
expr = 5*x**2 + 10*x - 30
roots = [N(root) for root in solve(expr)]
print("Корни функции:", roots)

derivative = diff(expr, x)
increasing = solve(derivative > 0)
print("Интервалы возрастания функции равны:", increasing)

decreasing = solve(derivative < 0)
print("Интервалы, на которых функция убывает, равны:", decreasing)

x_vals = np.linspace(-10, 10, 1000)
y_vals = 5*x_vals**2 + 10*x_vals - 30
plt.plot(x_vals, y_vals, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x) = 5x^2 + 10x - 30')
plt.grid(True)
plt.show()

top = N(simplify(-diff(expr, x)/(2*5)))
print("Вершина функции находится в x =", top)

positive = solve(expr > 0)
print("Интервалы, на которых функция положительна, равны:", positive)

negative = solve(expr < 0)
print("Интервалы, на которых функция отрицательна, равны:", negative)
