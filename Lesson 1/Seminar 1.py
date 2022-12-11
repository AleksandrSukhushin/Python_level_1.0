# Семинар 1 - Знакомство с языком Python

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#     *Примеры:*
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a == b**2 or b == a**2:
#     print('Ответ: да')
# else:
#     print('Ответ: нет')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# d = int(input('Введите число d: '))
# e = int(input('Введите число e: '))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print(max)

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
# d = int(input('Введите число d: '))
# e = int(input('Введите число e: '))

# list = [a,b,c,d,e]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)

my_list = []

for i in range(5):
    number = int(input(f'Введите {i+1} число: '))
    my_list.append(number)
print(my_list)

max = my_list[0]

for item in my_list:
    if item > max:
        max = item

print(f'В данном списке максимальное число: {max}')
