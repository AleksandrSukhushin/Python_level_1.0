# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Введите число n: '))
negofi_num = [1,-1]
fi_num = [1,1]

for i in range(2, number):
    fi_list = fi_num[i-1] + fi_num[i-2]
    fi_num.append(fi_list)
    negofi_list = negofi_num[i-2] - negofi_num[i-1]
    negofi_num.append(negofi_list)

negofi_num.reverse()
negofi_num.append(0)

print(f'Для n = {number} список чисел Негафибоначчи равен: {negofi_num + fi_num}')
