# Задача 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Мое решение:
# aX = int(input('Введите значение aX: '))
# aY = int(input('Введите значение aY: '))
# bX = int(input('Введите значение bX: '))
# bY = int(input('Введите значение bY: '))
# distance = round((((aX - bX)**2) + ((aY - bY)**2))**0.5, 1)
# print(f'Раастояние между точками A {aX,aY} и B {bX,bY} равно {distance}')

# Разбор задания с преподавателем:
import math
first = input('Введите координаты точки А через пробел: ').split(' ')
second = input('Введите координаты точки B через пробел: ').split()
distance = (float(first[0]) - float(second[0]))**2 + (float(first[1]) - float(second[1]))**2
# print(f'Расстояние между точками = {round(math.sqrt(distance), 2)}')
print(f'Расстояние между точками = {round((distance**0.5), 2)}')
