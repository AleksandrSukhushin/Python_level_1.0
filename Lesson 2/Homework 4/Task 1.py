# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.

# Задача А

from random import randint

k = int(input('Введите натуральную степень k: '))

# Запись в файл
def write_to_file(a):
    with open('first_polynomial.txt', 'w') as file:
        file.write(a)

# Создание коэффицентов в количестве k
def list_creation(k):
    list = []
    for _ in range(k + 1):
        list.append(randint(0, 101))
    return list

# Формирование первого многочлена
def first_polynomial(b):
    list = b[::-1]
    polynomial = ''
    if len(list) < 1:
        polynomial = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                polynomial += f'{list[i]}x**{len(list) - i - 1}'
                if list [i + 1] != 0:
                    polynomial += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                polynomial += f'{list[i]}x'
                if list[i + 1] != 0:
                    polynomial += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                polynomial += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                polynomial += ' = 0'
    return polynomial

coefficient = list_creation(k)
write_to_file(first_polynomial(coefficient))

# Задача B. Добавление второго многочлена и сложение его с ранее полученным

# Тут я уже либо сильно устал, либо что-то еще, но не долгнал, как можно сгенерить второй полином
with open('second_polynomial.txt', 'w') as file:
    file.write('23x**2 + 9x - 80 = 0')

with open('first_polynomial.txt','r') as file:
    first_polynomial = file.readline()

with open('second_polynomial.txt','r') as file:
    second_polynomial = file.readline()

# Изначально хотел привести оба полинома к списку, а дальше попробовать через условия сложить коэффициенты,
# но успехом не увенчалось, к сожалению ...
with open('total_polynomial.txt', 'w') as file:
    file.write(f'[{first_polynomial}] + [{second_polynomial}]')
