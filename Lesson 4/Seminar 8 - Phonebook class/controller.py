# Модуль управления функционалом

import view
import model

def start():
    pb = model.Phonebook()
    choice = ''
    while True:
        choice = view.main_menu()
        match choice:

            # 1 - Открыть файл:
            case 1:
                pb.open()
                view.information('\nФайл успешно открыт\n')

            # 2 - Сохранить файл:
            case 2:
                pb.save()
                view.information('\nФайл успешно сохранен\n')

            # 3 - Показать все контакты:
            case 3:
                view.show_contacts(pb.get())

            # 4 - Создать контакт:
            case 4:
                new_contact = list(view.create_new_contact())
                pb.new(new_contact)
                view.information(f'\nКонтакт {new_contact[0]} успешно создан\n')

            # 5 - Удалить контакт:
            case 5:
                del_contact = view.select_contact('Введите удаляемый контакт: ')
                contact = pb.get_contact(del_contact)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        pb.delete(contact[0])
                        view.information(f'\nКонтакт {contact[0][0]} успешно удален\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()

            # 6 - Изменить контакт:
            case 6:
                rename = view.select_contact('Введите изменяемый контакт: ')
                contact = pb.get_contact(rename)
                if contact:
                    changed_contact = view.change_contact()
                    pb.change(contact[1], list(changed_contact))
                    view.information(f'\nКонтакт {contact[0][0]} успешно изменен\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()

            # 7 - Найти контакт:
            case 7:
                find = view.find_contact()
                result = pb.search(find)
                view.show_contacts(result)

            # 8 - Выход из программы:
            case 8:
                view.end_program()
                break

            # Вывод ошибки некоректности введенных данных
            case _:
                view.input_eror()
