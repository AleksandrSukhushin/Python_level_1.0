# Модуль описания модели программы

class Phonebook:
    phone_book = []
    path: str

    def __init__(self, path: str = 'Lesson 4\Seminar 7 - Phonebook\data.txt'):
        self.path = path

    def get(self):
        return self.phone_book

    # 1 - Открыть файл
    def open(self):
        with open(self.path, 'r', encoding = 'UTF-8') as data:
            file = data.readlines()
        for contact in file:
            self.phone_book.append(contact.strip().split(';'))

    # 2 - Сохранить файл
    def save(self):
        pb_str = []
        for contact in self.phone_book:
            pb_str.append(';'.join(contact))
        with open(self.path, 'w', encoding = 'UTF-8') as data:
            data.write('\n'.join(pb_str))

    # 4 - Добавить новый контакт
    def new(self, new_contact: list):
        self.phone_book.append(new_contact)

    # Функция определения контакта
    def get_contact(self, text: str):
        result = []
        for i, contact in enumerate(self.phone_book):
            for field in contact:
                if text in field:
                    result.append((contact, i))
                    break
        if len(result) > 1:
            return False
        elif result == []:
            return result
        else:
            return result[0]

    # 7 - Поиск контакта
    def search(self, find: str):
        result = []
        for contact in self.phone_book:
            for field in contact:
                if find in field:
                    result.append(contact)
                    break
        return result

    # 5 - Функция удаления контакта
    def delete(self, contact: list):
        self.phone_book.remove(contact)

    # 5 - Функция изменения контакта
    def change(self, index: int, new: list):
        self.phone_book[index][0] = new[0] if new[0] != '' else self.phone_book[index][0]
        self.phone_book[index][1] = new[1] if new[1] != '' else self.phone_book[index][1]
        self.phone_book[index][2] = new[2] if new[2] != '' else self.phone_book[index][2]
