# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import *

length = int(input('Введите длину списка: '))
my_list = []
summa = 0

for i in range(length):
    number = random.randint(0,10)
    my_list.append(int(number))
    if i % 2 != 0:
        summa += my_list[i]

print(f'Сумма элементов списка: {my_list}, стоящих на позиции с нечетным индексом, равна: {summa}')
