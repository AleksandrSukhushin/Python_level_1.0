# Задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Мое решение:
# X = int(input('Введите значение X: '))
# Y = int(input('Введите значение Y: '))
# Z = int(input('Введите значение Z: '))
# for X in range(2):
#     for Y in range(2):
#         for Z in range(2):
#             print(not (X or Y or Z) == (not X and not Y and not Z))
#             print(X, Y, Z)

# Разбор задания с преподавателем:

flag = True
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            expression = not(x or y or z) == (not x and not y and not z)
            print(f'{x}\t{y}\t{z}\t{expression}')
