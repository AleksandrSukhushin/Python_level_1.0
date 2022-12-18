# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []

for _ in range(10):
    amount = random.randint(0,3)
    number = round(random.uniform(0,10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)

print(my_list)
