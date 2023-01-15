# List Comprehension, enumerate, lambda, zip, filter, map
# join - объединение объектов в одну строку!


# Задача 1. Напишите программу, которая удаляет из текста все слова, содержащие "абв"

# string = 'Питон - пожалуабвй лучший из лучшабвих языков программирования в мире!'
# # string = string.split()
# # new_list = list(filter(lambda word: not 'абв' in word, string.split()))
# new_list = [x for x in string.split() if not 'абв' in x]
# # for word in string:
# #     if not 'абв' in word:
# #         new_list.append(word)
# print(new_list)
# print(' '.join(new_list))

# Задача 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# path = r'Lesson 3\file.txt'
# with open(path, 'r') as data:
#     my_list = data.read().split()
# print(my_list)
# my_list = list(map(int, my_list))
# print(my_list)
# my_list = [my_list[x]-1 for x in range(1, len(my_list)) if my_list[x] - 1 != my_list[x-1]]
# print(my_list)
