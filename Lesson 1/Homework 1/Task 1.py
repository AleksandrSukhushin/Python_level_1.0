# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите номер дня недели от 1 до 7 включительно: '))
if 0 < number < 6:
    print('Будний день')
if number == 6 or number == 7:
        print('Выходной день')
elif 0 >= number or number > 7:
    print('Введите значение строго от 1 до 7!')
