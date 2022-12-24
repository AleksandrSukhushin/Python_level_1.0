# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Не удавшееся решение через цикл while:
# num = input('Введите вещественное число: ')
# sum = 0
# while num != 0:
#     sum += num % 10
#     num //= 10
# print(int(sum))

# Спустя какое-то время пришел к простейшему решению:
# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(f'Сумма цифр в числе {num} = {sum}')
# print(type(num))
# print(type(sum))

# Разбор решения с преподавателем
number = 'gerfbdg43556'
summa = 0
for char in number:
    if char.isdigit():
        summa += int(char)
print(summa)
