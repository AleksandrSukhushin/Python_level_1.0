# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Решение во 2 ДЗ:

# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(f'Сумма цифр в числе {num} = {sum}')
# print(type(num))
# print(type(sum))

# Решение сейчас с помощью List Comprehension:

print(sum([int(x) for x in input('Введите данные: ') if x.isdigit()]))
