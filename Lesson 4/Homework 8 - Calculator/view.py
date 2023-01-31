# Команды главного меню
commands = ['Enter a string expression to calculate', 'End']

# Функция вывода главного меню
def main_menu() -> int:
    print('Main menu\n')
    for i, item in enumerate(commands):
        print(f'\t{i+1}. {item}')
    while True:
        try:
            choice = int(input('\nSelect a menu item: '))
            print()
            if 0 < choice < 3:
                return choice
            else:
                print('\nEnter value 1 or 2!\n')
        except ValueError:
            print('\nPlease enter a valid value!\n')

# Функция ввода выражения
def input_list():
    my_list = input('Enter expression: ')
    my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    return my_list

# Функция выхода из программы
def end_program():
    print('\nSee you!\n')
