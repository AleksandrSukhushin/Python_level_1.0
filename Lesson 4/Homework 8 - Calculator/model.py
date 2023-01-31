global my_list

# Функция расчета
def calculate(my_list):
    while len(my_list) > 1:
        while '*' in my_list or '/' in my_list:
            i = 0
            while i < len(my_list):
                if my_list[i] == '*':
                    my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
                    my_list.pop(i)
                    my_list.pop(i)
                elif my_list[i] == '/':
                    my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
                    my_list.pop(i)
                    my_list.pop(i)
                i += 1
        while '+' in my_list or '-' in my_list:
            i = 0
            while i < len(my_list):
                if my_list[i] == '+':
                    my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
                    my_list.pop(i)
                    my_list.pop(i)
                elif my_list[i] == '-':
                    my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
                    my_list.pop(i)
                    my_list.pop(i)
                i += 1
    print(f'\nThe result of your expression: {my_list[0]}\n')
