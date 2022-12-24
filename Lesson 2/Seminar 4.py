# my_list = ['21', '543', 'fsd', 'esff3445']
# add = '-'
# print(add.join(my_list))

# my_dict = {32: '32', 543: '1', 'Ключ': 432314, 'Список': [432,543,4324,543]}
# # print(my_dict.get(32, 'Нет такого ключа'))
# my_dict['New'] = 'value'
# print(my_dict)

# my_dict = {}
# num_list = '4564354656345657567876456535476575456346456352234305938490382'
# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1
# print(my_dict)


my_list = 'A*x**2 + B*x + C = 0'

new_list = my_list.replace(' ', '').replace('=0', '')
new_list = new_list.split('+')
my_new_list = []

for i in new_list:
    my_new_list.append(i.split('*x')[0])

print(my_new_list)
