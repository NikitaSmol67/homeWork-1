# Задание №1
my_list = ['hello', 123 , True, 1.2, 21]
print(type(my_list))
x = len(my_list)
print(len(my_list))
while x != 0:
    print(type(my_list[x-1]))
    x = x - 1
# Задание №2 - warning
my_list =[]
x = None
while x != 'enough':
    my_list.append(x)
    x = input('Введите числа в список, если достаточно введите "enough" ')
if len(my_list) % 2 != 0:
    my_list.pop(0)
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    print(my_list)
else :
    my_list.pop(0)
    c = len(my_list)
    my_list.pop(c-1)
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(c)
    print(my_list)
# Задание №3
my_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август",
           "сентябрь", "октябрь", "ноябрь", "декабрь"]
x = int(input('Введите номер месяца '))
print(my_list[x-1])
my_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь",
           7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
x = int(input("Введите месяц "))
print(my_dict[x])
# Задание №4
my_list = list(input('Введите слова ').split(' '))
i = len(my_list)
numeric = 0
my_list.reverse()
while i != 0:
    i = i - 1
    numeric = numeric + 1
    print(numeric, my_list[i][0:10])
# Задание №5
my_list = [1, 7, 5, 3, 3, 2]
x = None
while x != 'enough':
    x = input('Введите число в список, если достаточно введите "enough" ')
    if x != 'enough':
        x = int(x)
        my_list.append(x)
        my_list.sort(reverse=True)
        print(my_list)
    else:
        print('Good job')
print(my_list)
# Задание 6
my_super_list = []
my_dict = {'Название':  '', 'цена': '', 'колличество': ''}
i = 1
my_list = [i]
print(my_dict)
while next != 'enough':
    x = input('Введите название для товара ')
    y = input('Введите цену для товра ')
    z = input('Введите колличество товара ')
    next = input('Next? Если достаточно введите "enough"')
    my_dict.update({'Название': x, 'цена': y, 'колличество': z})
    my_str = (i,  my_dict)
    i = i+1
    my_super_list.append(my_str)
    print(my_super_list)