# Задача 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

len_list = int(input('Введите количество элекментов списка: '))

import random
my_list = []
for i in range(len_list):
    my_list.append(random.randint(0, 100))
print(f'Исходный список:\t{my_list}')

for i in range(len_list-1, 0, -1):
    j = random.randint(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(f'Перемешанный список:\t{my_list}')
