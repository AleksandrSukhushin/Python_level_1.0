# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

length = int(input('Введите длину списка: '))
my_list = []
new_list = []

for i in range(length):
    amount = random.randint(0,3)
    number = round(random.uniform(0,10), amount)
    if number == int(number):
        my_list.append(int(number))
    else:
        my_list.append(number)

for i in my_list:
    if i % 1 != 0:
        new_list.append(round(i % 1, 3))
difference = round(max(new_list) - min(new_list), 3)

print(f'Исходный список: {my_list}\nДробная часть элементов из списка: {new_list}')
print(f'Разница между наибольшим и наименьшим значениями дробной части элементов списка: {difference}')
