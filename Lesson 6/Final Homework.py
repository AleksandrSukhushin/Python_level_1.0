# f(x) = -12x**4*sin(cos(x)) - 18x**3+5x**2 + 10x - 30

# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

# Построил график изначально самостоятельно при помощи материала предыдущего занятия и немного документации из библиотек
# import matplotlib.pyplot as plt
# import numpy as np

# def func(x):
#     return -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30

# x = np.linspace(-10, 10, 1000)
# y = [func(x) for x in x]

# plt.plot(x, y, 'r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('График функции: -12*x**4*sin(cos(x)) - 18*x**3+5x**2 + 10x - 30')
# plt.grid(True)
# plt.show()




# Но далее возникли проблемы с нахождением корней и тд, поэтому решил все-таки перейти в просмотру семинара
# Единственное, что сделал, поигрался с визуалом графика
import numpy as np
import matplotlib.pyplot as plt

limit = 10
step = 0.01
color = 'b'
line_s = '-'
direct_up = True

a, b, c, d, e = -12, -18, 5, 10, -30

x = np.arange(-limit, limit, step)

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def switch_line():
    global line_s
    if line_s == '-':
        line_s = '--'
    else:
        line_s = '-'
    return line_s

def func(x):
    return a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e

x_change = [(-limit, 'limit')]

for i in range(len(x) - 1):
    if (func(x[i]) > 0 and func(x[i + 1]) < 0) or (func(x[i]) < 0 and func(x[i + 1]) > 0):
        x_a = np.arange(x[i], x[i+1], 0.0000001)
        for j in range(len(x_a) - 1):
            if (func(x_a[j]) > 0 and func(x_a[j + 1]) < 0) or (func(x_a[j]) < 0 and func(x_a[j + 1]) > 0):
                x_change.append((x_a[j] if abs(0 - x_a[j]) < abs(0 - x_a[j+1]) else x_a[j+1], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i + 1]):
            x_a = np.arange(x[i], x[i + 1], 0.0000001)
            for j in range(len(x_a) - 1):
                if func(x_a[j]) > func(x_a[j + 1]):
                    x_change.append((x_a[j], 'direct'))
                    direct_up = False
                    break
    else:
        if func(x[i]) < func(x[i + 1]):
            x_a = np.arange(x[i], x[i + 1], 0.0000001)
            for j in range(len(x_a) - 1):
                if func(x_a[j]) < func(x_a[j + 1]):
                    x_change.append((x_a[j], 'direct'))
                    direct_up = True
                    break

x_change.append((limit, 'limit'))

print(x_change)
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct','limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]

roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'yo')

plt.plot(min_x, min_y, 'go', label = f'Экстремум функции: ({round(min_x, 2)}, {round(min_y, 2)})')
plt.plot(0, 0, 'yo', label = 'Корни функции:\n'
                                  f'({", ".join(roots)})')
plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label = 'Убывание > 0')
plt.plot(0, 0, 'r', label = 'Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label = 'Убывание < 0')
plt.plot(0, 0, 'r', label = 'Возрастание < 0')
plt.title(f'График f(x) = -12x^4sin(cos(x)) - 18x^3+5x^2 + 10x - 30')
plt.legend()
plt.show()
