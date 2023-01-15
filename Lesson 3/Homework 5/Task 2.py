# Задача 2.
# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

cell = list(range(1, 10))
combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# Функция ввода поля ячеек
def creation_field():
    print('-------------')
    for i in range(3):
        print('|', cell[0 + i*3], '|', cell[1 + i*3], '|', cell[2 + i*3], '|')
        print('-------------')

# Функция выбора ячейки
def selection_cell(player_turn):
    while True:
        value = input('Куда поставить ' + player_turn + ' ? ')
        if not (value in '123456789'):
            print('Укажите существующую ячейку!')
            continue
        value = int(value)
        if str(cell[value - 1]) in 'XO':
            print('Укажите свободную ячейку!')
            continue
        cell[value - 1] = player_turn
        break

# Функция проверки победителя
def check_winner():
    for i in combinations:
        if (cell[i[0] - 1]) == (cell[i[1] - 1]) == (cell[i[2] - 1]):
            return cell[i[1] - 1]
    else:
        return False

# Функция хода и завершения игры
def game_ower():
    counter = 0
    while True:
        creation_field()
        if counter % 2 == 0:
            selection_cell('X')
        else:
            selection_cell('O')
        if counter > 3:
            result = check_winner()
            if result:
                creation_field()
                print(result, 'победили!')
                break
        counter += 1
        if counter > 8:
            creation_field()
            print('Ничья!')
            break
game_ower()
