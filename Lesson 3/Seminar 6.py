# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

# Задача 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# Вариант 1
# my_list, my_dict, new_list = [1, 2, 3, 5, 1, 5, 3, 10], {}, []

# for i in range(len(my_list)):
#     my_dict[my_list[i]] = my_dict.get(my_list[i], 0) + 1

# for key, item in my_dict.items():
#     if item == 1:
#         new_list.append(key)
# print(new_list)

# Вариант 2
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# for i in my_list:
#     if my_list.count(i) == 1:
#         print(i)

# Вариант 3
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = [x for x in my_list if my_list.count(x) == 1]
# print(new_list)

# Задача 2.
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Длинный вариант решения
# my_list = input('Введите выражение: ')
# my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
# print(my_list)
# # if my_list.startswith(' - '):
# #     my_list = '-' + my_list[3:]
# while len(my_list) > 1:
#     while '*' in my_list or '/' in my_list:
#         i = 0
#         while i < len(my_list):
#             if my_list[i] == '*':
#                 my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#                 my_list.pop(i)
#                 my_list.pop(i)
#             elif my_list[i] == '/':
#                 my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#                 my_list.pop(i)
#                 my_list.pop(i)
#             i += 1
#     while '+' in my_list or '-' in my_list:
#         i = 0
#         while i < len(my_list):
#             if my_list[i] == '+':
#                 my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#                 my_list.pop(i)
#                 my_list.pop(i)
#             elif my_list[i] == '-':
#                 my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#                 my_list.pop(i)
#                 my_list.pop(i)
#             i += 1
# print(my_list)

# Короткий вариант решения
# my_list = input('Введите выражение: ')
# my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
# print(my_list)
# new_list = my_list.copy()
# oper = {'+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y,}
# def calculate(operation1, operation2):
#     i = 0
#     while operation1 in my_list or operation2 in my_list:
#         if my_list[i] in [operation1,operation2]:
#             my_list[i-1] = oper.get(my_list[i])(int(my_list[i-1]), int(my_list[i+1]))
#             my_list.pop(i)
#             my_list.pop(i)
#         else:
#             i += 1
# while len(my_list) > 1:
#     calculate('*', '/')
#     calculate('+', '-')
# print(f'{" ".join(new_list)} = {my_list[0]}')
