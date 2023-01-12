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

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)
