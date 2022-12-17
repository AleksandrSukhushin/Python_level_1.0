# Задача 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# при 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите целое число: '))
# my_list = []
# for i in range(-number, number + 1):
#     my_list.append(i)
# print(*my_list, sep = ', ')


# Задача 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#Примеры:
#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3

# Решение 1:
# number = float(input("Введите дробное число: "))
# if number == int(number):
#     print('Нет')
# else:
#     print(int(number * 10 % 10))

# Решение 2:
# number = input('Введите дробное число: ')
# print(number)
# number = number.split('.')
# print(number)
# if len(number) > 1:
#     print(number[1][0])
# else:
#     print('Целое число')

# Задача 3. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 10 или 15, но не 30.

# num = int(input('Введите целое число: '))
# if (num%10 == 0 or num%15 == 0) and not num%30 == 0:
#     print('Условие выполнено')
# else:
#     print('Условие НЕ выполнено')


# Задача 4. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# number = int(input('Введите число: '))
# my_list = []
# x = 1
# for i in range(1, number+1):
#     my_list.append(x)
#     x *= -3
# # number = int(input('Введите число: '))
# # for i in range(0, number):
# #     my_list.append((-3)**i)
# print(*my_list, sep = ', ')

# Библиотека Random
import random
my_list = []
for i in range(10):
    my_list.append(random.randint(0,100))
print(my_list)
random.shuffle(my_list)
print(my_list)
