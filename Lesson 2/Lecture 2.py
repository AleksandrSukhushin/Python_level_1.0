# Лекция 2. Данные, функции и модули в Python

# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'w')
# data.writelines(colors) #разделителей не будет
# data.writelines('\nLINE 2\n')
# data.writelines('LINE 3\n')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()


# import Lecture 1 as h
# print(h.f(1))

# Функция (рекурсия) - числа Фиббоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - некий "неитзменяемый" список
# a = (3, 4)
# print(a)
# print(a[0])

#Словари
# dict = {}
# dict = \
#     {
#         '1': '15',
#         '2': '17',
#         '3': '99',
#         '4': '13',
#     }
# # print(dict)
# # print(dict['3'])

# for k in dict.values():
# # for k in dict.keys():
#     print(k)

#Множества:
# numbers = {'1', '2', '3', '5'}
# print(type(numbers))
# print(numbers)

# #Списки:
# list1 = [1,2,3,4,5]
# print(len(list1))
# print(list1.pop())
# print(list1)
# # list2 = list1
# list1[0] = 123
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
