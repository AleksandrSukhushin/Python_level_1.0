# Типы данных и переменная
# int, float, boolean, str, list, None

# 1. Переменные:
# value = None
# print(type(value))
# a = 123
# b = 123.5
# # print(type(a))
# # print(type(b))
# # value = 123456
# # print(type(value))

# Строки:
# s = 'Hello world'
# print(a, '-', b, '-', s)

# Логическая переменная
# f = False
# print(f)

# Переменная list
# list['1', '2', '3']
# print(list)

# print('Введите a: ')
# a = int(input())
# print('Введите b: ')
# b = int(input())
# print (a, ' + ', b, ' = ', a+b)

# 2. Арифметические операции:
# a = 1.4532424532
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5
# print(a)

# 3. Логические операции:
# a = 1 < 4 and 5 > 2
# print(a)

# f = 1 > 2 and 4 < 6
# print(f)
# func = 1
# T = 4
# x = 2
# # a = 1 < 3 < 5
# print (func<T>x)

# f = [1,2,3,4]
# # print(f)
# # print(not 5 in f)

# is_odd = f[1] % 2
# print(is_odd)

# Управляющие конструкции if, if-else, while, for, while-else
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Это не Маша :(')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Ты кто?')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print('Пожалуй, хватит')
# print(inverted)

# r = range(10)
# for i in r:
#     print(i)

# 4. Работа со строками:

# help(list) - попросить пояснить любую функцию

# text = 'съешь еще этих мягких французских булок'
# print(len(text))

# 5. Фунции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 4.56

# print(f(arg))
# print(type(f(arg)))
