# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

length = int(input('Введите длину списка: '))
my_list = []
multi_list = []

for i in range(length):
    my_list.append(random.randint(0,10))

for i in range(length):
    while i < len(my_list)/2 and length > len(my_list)/2:
        length -= 1
        value = my_list[i] * my_list[length]
        multi_list.append(value)
        i += 1

print(f'Исходный список:\t{my_list}\nПеремноженный список:\t{multi_list}')
