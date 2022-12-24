# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число n элементов списка: '))
# list = [round((1 + 1 / i)**i, 2)
#     for i in range(1, n + 1)]
# print('Элементы списка вычисляются по формуле: (1 + 1/n)^n')
# print(f'Список из n элементов: {list}')
# print(f'Сумма n элементов списка: {round(sum(list), 2)}')

# Разбор решения с преподавателем:
number = int(input('Введите число n элементов списка: '))
my_list = []
for n in range(1, number + 1):
    num = round((1+1/n)**n,2)
    if num != int(num):
        my_list.append(num)
    else:
        my_list.append(int(num))
    # my_list.append(num if num != int(num) else int(num))
print(f'При n={number} список -> ', end='')
print(*my_list, sep=', ')
print(f'И его сумма -> {sum(my_list)}')
