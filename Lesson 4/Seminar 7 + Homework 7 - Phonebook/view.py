# Модуль пользовательского интерфейса

commands = ['Открыть файл', 'Сохранить файл', 'Показать все контакты', 'Создать контакт',
'Удалить контакт', 'Изменить контакт', 'Найти контакт', 'Выход из программы']

# Главное меню
def main_menu() -> int:
    print('Главное меню:')
    for i, item in enumerate(commands):
        print(f'\t{i+1}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('Введите значение от 1 до 8')
        except ValueError:
            print('Введите корректное значение')

# 3 - Показать контакты
def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('\nТелефонная книга пуста или не открыта\n')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:13} {contact[2]:20}')
        print()

# Ошибка ввода
def input_eror():
    print('\nОшибка ввода. Введите корректный пункт меню\n')

def empty_request():
    print('Искомый контакт не найден')

def many_request():
    print('Введите более точные данные. Найдено более 1 контакта!')

# Функция выхода из программы
def end_program():
    print('До свидания! Программа завершена.')

# 4 - Создать новый контакт
def create_new_contact():
    name = input('\nВведите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

# 5 - Функция удаления контакта
def select_contact(message: str):
    contact = input(message)
    return contact

# Подтверждение удаления контакта
def delete_confirm(contact: str):
    result = input(f'Вы действительно хотите удалить {contact}? (yes/no): ').lower()
    if result == 'yes':
        return True
    else:
        return False

# Функция изменения контакта
def change_contact():
    print('Введите новые данные (если изменения не требуются, нажмите Enter)')
    name = input('\nВведите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

# 7 - Поиск контакта
def find_contact():
    find = input('Введите искомый элемент: ')
    return find

# Вывод информации о завершении операции
def information(message):
    print(message)
