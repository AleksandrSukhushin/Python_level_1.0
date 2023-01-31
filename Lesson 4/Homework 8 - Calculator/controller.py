# Модуль управления калькулятором
import view
import model

def start():
    global my_list
    global new_list
    print('\nWelcome to string calculator!\n')
    choice = ''
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_list = view.input_list()
                model.calculate(my_list)
                break
            case 2:
                view.end_program()
                break
