# Модуль управления функционалом

import view
import model

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:

            # 1 - Открыть файл:
            case 1:
                model.open_file()

            # 2 - Сохранить файл:
            case 2:
                model.save_file()

            # 3 - Показать все контакты:
            case 3:
                view.show_contacts(model.get_phone_book())

            # 4 - Создать контакт:
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)

            # 5 - Удалить контакт:
            case 5:
                pass

            # 6 - Изменить контакт:
            case 6:
                pass

            # 7 - Найти контакт:
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)

            # 8 - Выход из программы:
            case _:
                view.input_eror()
