# Exercise №1
def my_func(var_1, var_2):
    if var_2 == 0:
        try:
            x = var_1 // 0
        except ZeroDivisionError:
            x = 0
    else:
        x = var_1 / var_2
    return x
number_1 = int(input('Введите число '))
number_2 = int(input('Введите число '))
print('Задание 1')
print(my_func(number_1, number_2))
# Exercise №2
def my_func_1(var_2, var_1, var_3, var_4, var_5, var_6):
    var_1 = input('Введите имя ')
    var_2 = input('Введите фамилию ')
    var_3 = input('Введите год рождения ')
    var_4 = input('Введите город проживания ')
    var_5 = input('Введиет email ')
    var_6 = input('Введите телефон ')
    return var_2, var_1, var_3, var_4, var_5, var_6
print('Задание 2')
print(my_func_1(var_1=10, var_2=12, var_3=13, var_4=14, var_5=15, var_6=11))
# Exercise №3
def my_func_3(var_1, var_2, var_3):
    if (var_1 + var_2) > (var_2 +var_3):
        x = (var_1+var_2)
    else :
        x = var_2 + var_3
    if x > (var_3 + var_1):
        x = x
    else:
        x = var_3 + var_1
    return x
print('Задание 3')
print(my_func_3(1, 4, 3))
# Exercise 4
def my_func_4(var_1, var_2):
    result = var_1 ** var_2
    return result
print('Задание 4')
print(my_func_4(3, -1))
def my_func_4_1(var_1,var_2):
    res = 1
    for i in range(abs(var_2)):
        res *= var_1
    if var_2 >= 0:
        return res
    else:
        return 1 / res
print(my_func_4_1(3, -2))
# Exercise 5
def my_func_5(*args):
    x = input('Введите числа ').split()
    y = len(x)
    sum = 0
    while y != 0 :
        y = y - 1
        b = int(x[y])
        sum += b
    return sum
print('Задание 5')
print(my_func_5('next'))
# Exercise 6
def int_func(var_1):
    var_1 = var_1.title()
    return var_1
print('Задание 6')
print(int_func('text notext super'))
def int_func(var_1):
    var_1 = var_1.title()
    return var_1
print(int_func(input('Введите слова в нижнем регистре ')))
