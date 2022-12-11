# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input('Введите значение X: '))
Y = int(input('Введите значение Y: '))

if X > 0 and Y > 0:
    print('Координата точки находится в 1 четверти плоскости')
elif X < 0 and Y > 0:
    print('Координата точки находится во 2 четверти плоскости')
elif X < 0 and Y < 0:
    print('Координата точки находится в 3 четверти плоскости')
elif X > 0 and Y < 0:
    print('Координата точки находится в 4 четверти плоскости')
elif X == 0 or Y == 0:
    print('Значение X и Y не должны быть равны 0!')
