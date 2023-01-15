# Задача 3.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#    Пример:
#       aaaaabbbcccc -> 5a3b4c
#       5a3b4c -> aaaaabbbcccc

# Первичные данные для кодировки и их считывание
with open('first_decode.txt', 'w') as data:
    data.write(input('Данные для кодировки: '))
with open('first_decode.txt', 'r') as data:
    first_data = data.read()

# Функция кодирование
def encode(first_data):
    encoding = ''
    preceding = ''
    count = 1
    if not first_data:
        return ''
    for i in first_data:
        if i != preceding:
            if preceding:
                encoding += str(count) + preceding
            count = 1
            preceding = i
        else:
                count += 1
    else:
        encoding += str(count) + preceding
        return encoding
data_encode = encode(first_data)

# Запись результата кодирования и его считывание для последующего декодирования
with open('only_encode.txt', 'w') as data:
    data.write(data_encode)
with open('only_encode.txt', 'r') as data:
    second_data = data.read()

# Функция декодирования
def decode(second_data):
    decoding = ''
    count = ''
    for i in second_data:
        if i.isdigit():
            count += i
        else:
            decoding += i * int(count)
            count = ''
    return decoding
data_decode = decode(second_data)

# Запись результата декодирования
with open('second_decode.txt', 'w') as data:
    data.write(data_decode)
with open('second_decode.txt', 'r') as data:
    second_data = data.read()

# Проверки правильности выполнения кодирования и последующего декодирования первичных данных
result_RLE = [first_data[i] for i in range(len(second_data)) if second_data[i] == first_data[i]]
if result_RLE == list(second_data):
    print('Процесс кодирования и последующего декодирования прошел успешно :)')
else:
    print('Что-то пошло не так :(')
