# Лекция 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension


# def calc(op, a, b):
#     print(op(a, b))
# calc(lambda x, y: x+y+1, 4, 5)


# List Comprehension

# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list)

# Задачи!!!
# Number 1 - LAMBDA

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Number 2 - MAP

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)

# Number 3 - FILTER

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

# Вывод из 1 задачи:

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Number 4 - ZIP

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# data = list(zip(users, ids))
# print(data)

# Number 5 - ENUMERATE

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)

# from time import *
# iter = 33
# n = []
# n_a = 0
# n_b = 0
# t = perf_counter() # time()
# for i in range(1, iter):
#     for j in range(iter):
#         for k in range(iter):
#             for l in range(iter):
#                 n_a = i ** 3 + j ** 3
#                 n_b = k ** 3 + l ** 3
#                 if n_a == n_b and i != k and j != l and i != l and j != k:
#                     if not n_a in n:
#                         n.append(n_a)
#                         # print(n_a, i, j, k, l)
# n.sort()
# print(n, sep='\n')
# # print(time() - t)
# print(perf_counter() - t)


# for a in range(1, 33):
#     for b in range(33):
#         for c in range(33):
#             for d in range(33):
#                 if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
#                     print(a ** 3 + b ** 3)
