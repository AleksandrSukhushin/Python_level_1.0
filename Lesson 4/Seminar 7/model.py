# Модуль описания модели программы

phone_book = []
path = 'Lesson 4\Seminar 7 - Phonebook\data.txt'


def get_phone_book():
    global phone_book
    return phone_book

# 1 - Открыть файл
def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding = 'UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))

# 2 - Сохранить файл
def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding = 'UTF-8') as data:
        data.write('\n'.join(pb_str))

# 4 - Добавить новый контакт
def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

# 7 - Поиск контакта
def search_contact(find: str):
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result
