
commands = ['Открыть файл', 'Сохранить файл', 'Показать все контакты', 'Создать контакт',
'Удалить контакт', 'Изменить контакт', 'Найти контакт', 'Выход из программы']

# Главное меню
def main_menu() -> int:
    print('Главное меню:')
    for i, item in enumerate(commands):
        print(f'\t{i+1}. {item}')
    choice = int(input('Выберите пункт меню: '))
    return choice

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

# 4 - Создать новый контакт
def create_new_contact():
    name = input('\nВведите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

# 7 - Поиск контакта
def find_contact():
    find = input('Введите искомый элемент: ')
    return find
